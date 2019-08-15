import click
import logging
from alf import utils
from alf.commands.s3_client.s3_client import S3Client

logger = logging.getLogger(__name__)


@click.command('show',
               short_help='Show dataset via S3.')
@click.option('--s3_path',
              type=click.STRING,
              required=False,
              default='',
              help='Source name of S3.')
@click.option('--show_file',
              type=click.BOOL,
              required=False,
              default=False,
              help='Show list file by the folder.')
@click.option('--show_full_dir',
              type=click.BOOL,
              required=False,
              default=True,
              help='Show full path of the folder.')
def show(s3_path, show_file, show_full_dir):
    s3_client = S3Client(aws_access_key_id=utils.get_aws_access_key_id(),
                         aws_secret_access_key=utils.get_aws_secret_access_key(),
                         bucket=utils.get_aws_bucket())
    logger.warning("Wait a moment for display structure of '{}' bucket ...".format(utils.get_aws_bucket()))
    s3_client.show_structure(s3_path, show_file, show_full_dir)
    return 0
