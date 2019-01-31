# Copyright 2019 Google LLC
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

import pathlib
import tarfile

from docuploader import tar


def make_tree(root, tree):
    root = pathlib.Path(root)
    root.mkdir(parents=True, exist_ok=True)

    for key, value in tree.items():
        if isinstance(value, dict):
            make_tree(root / key, value)
        else:
            (root / key).write_text(value)


def test_tar(tmpdir):
    root = tmpdir / "tar_test_dir"
    make_tree(root, {"a.txt": "a", "subdir": {"b.txt": "b", "c.txt": "c"}})

    destination = tmpdir / "test.tar.gz"
    tar.compress(root, destination)

    assert tarfile.is_tarfile(destination)

    tf = tarfile.open(destination, "r:gz")
    files = sorted(tf.getnames())

    assert files == [".", "./a.txt", "./subdir", "./subdir/b.txt", "./subdir/c.txt"]

    assert tf.extractfile("./a.txt").read() == b"a"
