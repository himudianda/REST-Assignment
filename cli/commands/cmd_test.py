import logging
import subprocess
import click

from config import settings


TESTS_PATH = '{0}/{1}'.format(settings.APP_ROOT, '/server/tests')


@click.command()
@click.argument('path', default=TESTS_PATH)
def cli(path):
    """
    Run tests.

    :return: Subprocess call result
    """
    print TESTS_PATH
    cmd = 'py.test {0}'.format(path)

    print cmd
    return subprocess.call(cmd, shell=True)
