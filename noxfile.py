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

import nox

DEFAULT_PYTHON_VERSION = "3.9"

@nox.session(python=DEFAULT_PYTHON_VERSION)
def blacken(session):
    session.install('black')
    session.run('black', 'docuploader', 'tests')


@nox.session(python=DEFAULT_PYTHON_VERSION)
def lint(session):
    session.install('mypy', 'flake8', 'black', 'types-pkg_resources')
    session.run('pip', 'install', '-e', '.')
    session.run('black', '--check', 'docuploader', 'tests')
    session.run('flake8', 'docuploader', 'tests')
    session.run('mypy', 'docuploader')


@nox.session(python=DEFAULT_PYTHON_VERSION)
def test(session):
    session.install('pytest', 'pytest-cov')
    session.run('pip', 'install', '-e', '.')
    session.run('pytest', '--cov-report', 'term-missing', '--cov', 'docuploader', 'tests', *session.posargs)


@nox.session(python=DEFAULT_PYTHON_VERSION)
def generate_protos(session):
    session.install("grpcio-tools", "mypy-protobuf")
    session.run(
        "python", "-m", "grpc_tools.protoc",
        "-Idocuploader/protos",
        "--python_out=docuploader/protos",
        "--mypy_out=docuploader/protos",
        "docuploader/protos/metadata.proto")
