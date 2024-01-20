import hashlib
import os
import shlex
import subprocess
from pathlib import Path

import pytest

import client
import server as sfserver


def test_send_file(server_fixture):
    """ Send a 1 GB file from the client to the server. """
    filename = 'tmpfile.txt'
    tempfilepath = Path('test_files') / filename
    tempfilepath.parent.mkdir(parents=True, exist_ok=True)
    filesize = 1024 * 1024 * 1024  # 1GB
    create_file_with_random_bytes_of_size(tempfilepath, filesize)
    hash_client_file = get_md5(tempfilepath)
    client.send_file(tempfilepath.resolve())

    # Verify the md5 hash on the server side
    hash_server_file = get_md5(Path(sfserver.SAVE_FILEPATH) / filename)
    assert hash_client_file == hash_server_file


@pytest.fixture(scope="module")
def server_fixture():
    proc = subprocess.Popen(
        shlex.split('uvicorn main:app --host 0.0.0.0'),
        cwd=os.path.join('..', 'server'),
    )
    yield
    proc.kill()


def create_file_of_size(path, size):
    # Using this trick to create large files of arbitrary size:
    # https://stackoverflow.com/a/8816154
    print(f'Creating file with truncated bytes {path.resolve()} of size {size} bytes')
    with path.open('w') as f:
        f.truncate(size)


def create_file_with_random_bytes_of_size(path, size):
    print(f'Creating file with random bytes {path.resolve()} of size {size} bytes')
    with path.open('wb') as f:
        f.write(os.urandom(size))


def get_md5(path):
    # Python program to find MD5 hash value of a file
    md5_hash = hashlib.md5()
    with path.open('rb') as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096), b''):
            md5_hash.update(byte_block)
    return md5_hash.hexdigest()
