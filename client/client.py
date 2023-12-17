import os

import click
import requests

HOSTNAME = 'localhost'
PORT = '8000'


@click.command()
@click.argument('filepath', type=click.Path(exists=True))
def send_file_or_directory(filepath):
    """Send file or directory if it exists"""

    # If the path is a directory, we'll only send files in the top level.
    # Currently we only send the files in the directory.  The server
    # does not create the directory and put the files inside it.
    # TODO: Add support for -r

    # Count Files.  If > 9 files, get confirmation before sending
    if os.path.isdir(filepath):
        file_count = 0
        for path in os.listdir(filepath):
            if os.path.isfile(os.path.join(filepath, path)):
                file_count += 1

        print(f'File count is {file_count}')
        if file_count >= 10:
            response = input(f'Send {file_count} files? y/n: ')
            if not response.lower() == 'y':
                return

        for path in os.listdir(filepath):
            joined_path = os.path.join(filepath, path)
            if os.path.isfile(joined_path):
                send_file(joined_path)

        return

    # Send an individual file
    send_file(filepath)


def send_file(filepath):
    files = {'file': open(filepath, 'rb')}
    click.echo(f'Sending {os.path.abspath(click.format_filename(filepath))}', nl=False)
    req = requests.post(f'http://{HOSTNAME}:{PORT}/files', files=files)
    click.echo(f' ...Done')


if __name__ == '__main__':
    send_file_or_directory()