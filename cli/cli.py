import click
import os
import sys

cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'commands'))

class CLI(click.MultiCommand):
    def list_commands(self, ctx):
        commands = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and filename.startswith('cmd_'):
                commands.append(filename[4:-3])
        commands.sort()
        return commands

    def get_command(self, ctx, name):
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
            mod = __import__('cli.commands.cmd_' + name, None, None, ['cli'])
        except ImportError as e:
            exit(1)

        return mod.cli

@click.command(cls=CLI)
def cli():
    """ Commands to help manage the project """
    pass
