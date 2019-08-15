import click
import os
from alf import utils
from alf.commands.s3_client.s3_client import S3Client


@click.command('download',
               short_help='Download dataset via S3.')
@click.option('--s3_path',
              type=click.STRING,
              default='',
              help='Path to get the dataset')
@click.option('--local_path',
              type=click.Path(exists=True, resolve_path=True),
              default='.',
              help='Path to save the downloaded dataset')
def download(s3_path, local_path):
    s3_client = S3Client(aws_access_key_id=utils.get_aws_access_key_id(),
                         aws_secret_access_key=utils.get_aws_secret_access_key(),
                         bucket=utils.get_aws_bucket())

    print('Download data from: "{}" to: "{}"'.format(s3_path,
                                                     os.path.join(os.path.realpath(local_path),
                                                                  s3_path)))
    s3_client.download(s3_path, local_path)
