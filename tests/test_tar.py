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


def read_tree(root):
    root = pathlib.Path(root)
    result = {}
    for p in root.iterdir():
        if p.is_dir():
            result[p.name] = read_tree(p)
        else:
            with p.open() as f:
                result[p.name] = f.readline()
    return result


def test_tar(tmpdir):
    root = tmpdir / "tar_test_dir"
    in_tree = {"a.txt": "a", "subdir": {"b.txt": "b", "c.txt": "c"}}
    make_tree(root, in_tree)

    tar_destination = tmpdir / "test.tar.gz"
    tar.compress(root, tar_destination)

    assert tarfile.is_tarfile(tar_destination)

    decompress_destination = tmpdir / "tar_out_dir"
    pathlib.Path(decompress_destination).mkdir(parents=True, exist_ok=True)
    tar.decompress(tar_destination, decompress_destination)

    got_tree = read_tree(decompress_destination)
    assert got_tree == in_tree
