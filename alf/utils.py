import sys
from pathlib import Path

S3_ACCESS_PATH = Path.home() / '.s3_access'
S3_SECRET_PATH = Path.home() / '.s3_secret'
S3_BUCKET_PATH = Path.home() / '.s3_bucket'


def get_aws_access_key_id():
    try:
        return S3_ACCESS_PATH.open('r').readline().rstrip()
    except FileNotFoundError as e:
        print('ACCESS key not found, set up with:\033[1m configure --key <ACCESS KEY>\033[0m')
        sys.exit(-1)


def get_aws_secret_access_key():
    try:
        return S3_SECRET_PATH.open('r').readline().rstrip()
    except FileNotFoundError as e:
        print('SECRET key not found, set up with:\033[1m configure --key <SECRET KEY>\033[0m')
        sys.exit(-1)


def get_aws_bucket():
    try:
        return S3_BUCKET_PATH.open('r').readline().rstrip()
    except FileNotFoundError as e:
        print('BUCKET key not found, set up with:\033[1m configure --key <BUCKET KEY>\033[0m')
        sys.exit(-1)


def set_aws_access_key_id(key: str):
    S3_ACCESS_PATH.open('w').writelines([key])


def set_aws_secret_access_key(key: str):
    S3_SECRET_PATH.open('w').writelines([key])


def set_aws_bucket(key: str):
    S3_BUCKET_PATH.open('w').writelines([key])
