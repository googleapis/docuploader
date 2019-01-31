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

import sys
import tempfile

import click
import pkg_resources

import docuploader.credentials
import docuploader.log
import docuploader.tar
import docuploader.upload

try:
    VERSION = pkg_resources.get_distribution("gcp-docuploader").version
except pkg_resources.DistributionNotFound:
    VERSION = "0.0.0+dev"


@click.command()
@click.version_option(message="%(version)s", version=VERSION)
@click.option(
    "--credentials",
    default=docuploader.credentials.find(),
    help="Path to the credentials file to use for Google Cloud Storage.",
)
@click.argument("documentation_path")
# TODO: Metadata
def main(credentials, documentation_path):
    if not credentials:
        docuploader.log.error(
            "You need credentials to run this! Specify --credentials on the command line."
        )
        return sys.exit(1)

    docuploader.log.info(
        f"Sit tight, I'm tarring up your docs in {documentation_path}."
    )

    with tempfile.NamedTemporaryFile() as fh:
        fh.close()
        tar_filename = fh.name

        docuploader.tar.compress(documentation_path, tar_filename)

        docuploader.log.success(f"Cool, I have those tarred up.")

        docuploader.log.info(f"Okay, I'm sending them to the cloud™ now.")

        docuploader.upload.upload(
            source=tar_filename,
            # TODO: Destination filename should be based on metadata.
            destination="test.tar.gz",
            # TODO: Bucket should be an argument / well-known constant, I guess?
            bucket="docs-resources",
            credentials_file=credentials,
        )

    docuploader.log.success(f"All is well, your docs were uploaded! <3")


if __name__ == "__main__":
    main()
