# Copyright 2014 Florian Ludwig
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os
import tempfile
import subprocess
import atexit
import shutil
import argparse

import pkg_resources


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8000)
    parser.add_argument('--root', type=str, default='.')
    args = parser.parse_args()

    conf_template = pkg_resources.resource_string('nginc', 'nginx.conf')
    tmp = tempfile.mkdtemp(prefix='nginc')

    @atexit.register
    def cleanup():
        shutil.rmtree(tmp)

    root = os.path.abspath(args.root)
    config = conf_template.format(tmp=tmp, root=root, port=args.port)
    conf_path = tmp + '/nginx.conf'
    conf_file = open(conf_path, 'w')
    conf_file.write(config)
    conf_file.close()

    proc = subprocess.Popen(['nginx', '-c', conf_path])
    try:
        proc.wait()
    except KeyboardInterrupt:
        proc.kill()
