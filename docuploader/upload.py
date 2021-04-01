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

"""Handles uploading files to Google Cloud Storage."""

from google.cloud import storage
from google.auth.credentials import Credentials


def upload(
    *,
    source: str,
    destination: str,
    bucket: str,
    credentials: Credentials,
    project_id: str
) -> storage.Blob:
    client = storage.Client(project=project_id, credentials=credentials)
    bucket_ = client.get_bucket(bucket)
    blob = bucket_.blob(destination)
    blob.upload_from_filename(filename=source)
    return blob
