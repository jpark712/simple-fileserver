import requests


FILENAME = 'PATH_TO_FILE_NAME'
HOSTNAME = 'localhost'
PORT = '8000'


def main():
    files = {'file': open(FILENAME, 'rb')}
    req = requests.post(f'http://{HOSTNAME}:{PORT}/files', files=files)
    print('Done')


if __name__ == '__main__':
    main()