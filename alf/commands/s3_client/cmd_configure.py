import click
from alf import utils


@click.command('configure', short_help='Configure keys')
def configure():
    key = input('S3 ACCESS KEY: ')
    utils.set_aws_access_key_id(key)
    key = input('S3 SECRET ACCESS KEY: ')
    utils.set_aws_secret_access_key(key)
    key = input('S3 BUCKET: ')
    utils.set_aws_bucket(key)

