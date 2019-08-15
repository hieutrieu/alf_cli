import click
import os
from alf import utils
from alf.commands.s3_client.s3_client import S3Client


@click.command('upload',
               short_help='Upload dataset via S3.')
@click.option('--local_path',
              type=click.STRING,
              default='.',
              help='Path to get the dataset')
@click.option('--s3_path',
              type=click.STRING,
              default='',
              help='Path to save the dataset')
def upload(local_path, s3_path):
    s3_client = S3Client(aws_access_key_id=utils.get_aws_access_key_id(),
                         aws_secret_access_key=utils.get_aws_secret_access_key(),
                         bucket=utils.get_aws_bucket())

    print('Upload data from: "{}" to: "{}"'.format(os.path.join(os.path.realpath(s3_path),
                                                                local_path),
                                                   local_path))
    s3_client.upload(local_path, s3_path)
