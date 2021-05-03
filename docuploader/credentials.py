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

"""Helper for finding credentials.

When running this tool, there are two possible scenarios:

1. The tool is running as part of CI to publish the docs. In that case,
   credentials should be at a well-known location or use ADC.
2. The tool is running locally as part of development. In that case,
   the credentials should be passed into the command-line or via ADC.

(2) takes precedence. Command-line params also override local files.
"""

import os
from typing import List, Optional

from google.oauth2 import service_account
import google.auth

_WELL_KNOWN_LOCATIONS: List[str] = []

if "KOKORO_KEYSTORE_DIR" in os.environ:
    _WELL_KNOWN_LOCATIONS.append(
        os.path.join(
            os.environ["KOKORO_KEYSTORE_DIR"], "73713_docuploader_service_account"
        )
    )


def find_path():
    for location in _WELL_KNOWN_LOCATIONS:
        if os.path.exists(location):
            return location
    return ""


def find(credentials_file: Optional[str] = ""):
    if not credentials_file:
        credentials_file = find_path()

    if credentials_file != "":
        credentials = service_account.Credentials.from_service_account_file(
            credentials_file
        )
        return credentials, credentials.project_id
    else:
        return google.auth.default()
