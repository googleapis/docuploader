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

import click
import pkg_resources

import docuploader.credentials
import docuploader.log

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
def main(credentials):
    if not credentials:
        docuploader.log.error(
            "You need credentials to run this! Specify --credentials on the command line."
        )
        return sys.exit(1)

    docuploader.log.success(f"I don't do anything yet. :)")


if __name__ == "__main__":
    main()
