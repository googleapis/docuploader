# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import os
import pathlib
import shutil
import sys
import tempfile
from typing import List, Optional
from importlib.metadata import version, PackageNotFoundError

import click
from google.protobuf import text_format, json_format  # type: ignore

from docuploader.protos import metadata_pb2
import docuploader.credentials
import docuploader.log
import docuploader.tar
import docuploader.upload

try:
    VERSION = version("gcp-docuploader")
except PackageNotFoundError:
    VERSION = "0.0.0+dev"

DEFAULT_STAGING_BUCKET = "docs-resources"


@click.group()
@click.version_option(message="%(version)s", version=VERSION)
def main():
    pass


@main.command()
@click.option(
    "--staging-bucket",
    default=DEFAULT_STAGING_BUCKET,
    help="The bucket to upload the staged documentation to.",
)
@click.option(
    "--credentials",
    default=None,
    help="Path to the credentials file to use for Google Cloud Storage.",
)
@click.option(
    "--metadata-file",
    default=None,
    help="Path to the docs.metadata file. The path must be relative to the CWD.",
)
@click.option(
    "--destination-prefix",
    default=None,
    help="Prefix to include when uploading tar file. A - will be added after the prefix, if there is one.",
)
@click.option(
    "--project-id",
    default=None,
    help="Override the project ID for the GCS bucket.",
)
@click.argument("documentation_path")
def upload(
    staging_bucket: str,
    credentials: str,
    metadata_file: Optional[str],
    destination_prefix: str,
    documentation_path: str,
    project_id: Optional[str],
):
    gcp_credentials, adc_project_id = docuploader.credentials.find(credentials)
    if not gcp_credentials:
        docuploader.log.error(
            "You need credentials to run this! Use Application Default Credentials or specify --credentials on the command line."
        )
        sys.exit(1)

    # default to credentials' project ID
    gcs_project_id = project_id if project_id else adc_project_id

    if metadata_file is None:
        metadata_file = "docs.metadata"
        json_file = pathlib.Path(documentation_path) / "docs.metadata.json"
        if json_file.exists():
            metadata_file = "docs.metadata.json"
    metadata_path = pathlib.Path(metadata_file)

    if not metadata_path.exists():
        docuploader.log.error(
            "You need metadata to upload the docs. You can generate it with docuploader create-metadata"
        )
        sys.exit(1)
    try:
        if not os.listdir(documentation_path):
            docuploader.log.error(
                f"The documentation path given ({documentation_path}) does not contain any documentation files."
            )
            sys.exit(1)
    except FileNotFoundError:
        docuploader.log.error(
            f"The documentation path given ({documentation_path}) does not exist relative to CWD."
        )
        sys.exit(1)
    except NotADirectoryError:
        docuploader.log.error(
            f"The documentation path given ({documentation_path}) is a file not a directory."
        )
        sys.exit(1)

    docuploader.log.success("Let's upload some docs!")

    docuploader.log.info("Loading up your metadata.")

    if documentation_path not in metadata_file:
        shutil.copy(
            metadata_path,
            pathlib.Path(documentation_path) / metadata_file,
        )

    metadata = metadata_pb2.Metadata()
    if metadata_file.endswith(".json"):
        json_format.Parse(metadata_path.read_text(), metadata)
    else:
        text_format.Merge(metadata_path.read_text(), metadata)

    # Validating metadata for required fields

    # TODO: Do additional validiation
    if not metadata.name:
        raise Exception("Metadata field 'name' is required.")
    if not metadata.version:
        raise Exception("Metadata field 'version' is required.")
    if not metadata.language:
        raise Exception("Metadata field 'language' is required.")

    docuploader.log.success(
        f"Looks like we're uploading {metadata.name} version {metadata.version} for {metadata.language}."
    )

    docuploader.log.info(
        f"Sit tight, I'm tarring up your docs in {documentation_path}."
    )

    with tempfile.NamedTemporaryFile() as fh:
        fh.close()
        tar_filename = fh.name
        docuploader.tar.compress(documentation_path, tar_filename)
        docuploader.log.success("Cool, I have those tarred up.")
        docuploader.log.info("Okay, I'm sending them to the cloud™ now.")
        destination_name = (
            f"{metadata.language}-{metadata.name}-{metadata.version}.tar.gz"
        )
        if destination_prefix:
            #  destination_prefix should end in alphanumeric character
            while not destination_prefix[-1].isalnum():
                destination_prefix = destination_prefix[:-1]

            destination_name = f"{destination_prefix}-{destination_name}"

        docuploader.upload.upload(
            source=tar_filename,
            destination=destination_name,
            bucket=staging_bucket,
            credentials=gcp_credentials,
            project_id=gcs_project_id,
        )

    docuploader.log.success(
        f"All is well, your docs were uploaded to gs://{staging_bucket}/{destination_name}! <3"
    )


@main.command()
# TODO: Use https://github.com/googleapis/protoc-docs-plugin to add docstrings
# to the pb2 module so that I can reference them here.
@click.option("--name", required=True)
@click.option("--version", required=True)
@click.option("--language", required=True)
@click.option("--distribution-name", default="")
@click.option("--product-page", default="")
@click.option("--github-repository", default="")
@click.option("--issue-tracker", default="")
@click.option("--stem", default="")
@click.option("--serving-path", default="")
@click.option("--xrefs", multiple=True, default=[])
@click.option("--xref-services", multiple=True, default=[])
@click.argument("destination", default="docs.metadata")
def create_metadata(
    name: str,
    version: str,
    language: str,
    distribution_name: str,
    product_page: str,
    github_repository: str,
    issue_tracker: str,
    destination: str,
    stem: str,
    serving_path: str,
    xrefs: List[str],
    xref_services: List[str],
):
    metadata = metadata_pb2.Metadata()
    metadata.update_time.FromDatetime(datetime.datetime.utcnow())
    metadata.name = name
    metadata.language = language
    metadata.version = version
    metadata.distribution_name = distribution_name
    metadata.product_page = product_page
    metadata.github_repository = github_repository
    metadata.issue_tracker = issue_tracker
    metadata.stem = stem
    metadata.serving_path = serving_path
    metadata.xrefs.extend(xrefs)
    metadata.xref_services.extend(xref_services)

    destination_path = pathlib.Path(destination)
    destination_path.write_text(text_format.MessageToString(metadata))
    docuploader.log.success(f"Wrote metadata to {destination_path}.")


if __name__ == "__main__":
    main()
