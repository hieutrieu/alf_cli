import click
import os
from pathlib import Path


class AlfCli(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filepath in Path(os.path.dirname(__file__), 'commands/s3_client').glob('*.py'):
            filename = filepath.stem
            if filename.startswith('cmd_'):
                rv.append(filename[4:])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            module = __import__('alf.commands.s3_client.cmd_' + name,
                                None, None, fromlist=[name])
        except ImportError:
            return None
        return module.__dict__[name]


cli = AlfCli(help='This tool\'s commands are loaded from a '
                  'plugin folder dynamically.')

if __name__ == '__main__':
    cli()


@click.command(cls=AlfCli)
def cli():
    pass
