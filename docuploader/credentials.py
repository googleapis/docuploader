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
   credentials should be at a well-known location.
2. The tool is running locally as part of development. In that case,
   the credentials should be passed into the command-line.

(2) takes precedence. Command-line params also override local files. This
module deals with (1), while __main__ handles (2).
"""

import os
from typing import List

_WELL_KNOWN_LOCATIONS: List[str] = []

if "KOKORO_KEYSTORE_DIR" in os.environ:
    _WELL_KNOWN_LOCATIONS.append(
        os.path.join(
            os.environ["KOKORO_KEYSTORE_DIR"], "73713_docuploader_service_account"
        )
    )


def find():
    for location in _WELL_KNOWN_LOCATIONS:
        if os.path.exists(location):
            return location
