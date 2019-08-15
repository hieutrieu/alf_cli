import click
from alf import utils
from alf.commands.s3_client.s3_client import S3Client


@click.command('delete',
               short_help='Delete source from S3.')
@click.option('--s3_path',
              type=click.STRING,
              required=False,
              default='',
              help='Source name of S3.')
def delete(s3_path):
    s3_client = S3Client(aws_access_key_id=utils.get_aws_access_key_id(),
                         aws_secret_access_key=utils.get_aws_secret_access_key(),
                         bucket=utils.get_aws_bucket())
    s3_client.delete(s3_path)
    return 0
