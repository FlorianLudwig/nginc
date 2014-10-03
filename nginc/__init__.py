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
