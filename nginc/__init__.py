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


def start(root, address='127.0.0.1', port=8000):
    conf_template = pkg_resources.resource_string('nginc', 'nginx.conf')
    conf_template = conf_template.decode('utf-8')
    tmp = tempfile.mkdtemp(prefix='nginc')

    @atexit.register
    def cleanup_tmp():
        shutil.rmtree(tmp)

    root = os.path.abspath(root)
    root = root.replace('"', '\\"')
    config = conf_template.format(tmp=tmp, root=root, port=port, address=address)
    conf_path = tmp + '/nginx.conf'
    conf_file = open(conf_path, 'w')
    conf_file.write(config)
    conf_file.close()

    proc = subprocess.Popen(['nginx', '-c', conf_path])
    @atexit.register
    def cleanup_proc():
        try:
            proc.kill()
        except OSError:
            pass

    return proc


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=8000,
                        help='port to bind to')
    parser.add_argument('-r', '--root', type=str, default='.',
                        help='directory to serve, defaults to current working directory')
    parser.add_argument('-a', '--address', type=str, default='127.0.0.1',
                        help='address to bind to')
    parser.add_argument('-A', action='store_true',
                        help='shortcut for --address 0.0.0.0')
    args = parser.parse_args()
    address = args.address
    if args.A:
        address = '0.0.0.0'

    proc = start(args.root, address, args.port)

    try:
        proc.wait()
    except KeyboardInterrupt:
        proc.kill()
