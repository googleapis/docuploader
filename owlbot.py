# Copyright 2020 Google LLC
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

import synthtool as s
from synthtool import gcp

common = gcp.CommonTemplates()

# ----------------------------------------------------------------------------
# Add templated files
# ----------------------------------------------------------------------------
templated_files = common.py_library()
s.move(
    templated_files,
    excludes=[
        ".flake8",
        ".trampolinerc",
        "MANIFEST.in",
        "setup.cfg",
        ".coveragerc",
        "noxfile.py",  # repo uses nox
        "docs/**/*",  # no docs to publish
        ".github/CODEOWNERS", # using custom CODEOWNERS for this repo
        ".kokoro/docs/",
        ".kokoro/docker/**",
        ".kokoro/publish-docs.sh",
        ".kokoro/samples/**", # no samples
        ".kokoro/test-sample*",
        "CONTRIBUTING.rst",  # repo has a CONTRIBUTING.md
        ".github/CONTRIBUTING.md",
        ".github/PULL_REQUEST_TEMPLATE.md",
        ".github/snippet-bot.yml",
        ".gitignore",
        ".github/workflows", # exclude templated gh actions
        "scripts/**",
        "testing/",
        "README.rst",
    ],
)
s.shell.run(["nox", "-s", "generate_protos", "blacken"], hide_output=False)
