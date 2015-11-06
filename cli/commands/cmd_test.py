import subprocess
import click

from config import settings


APP_ROOT = settings.APP_ROOT
TESTS_PATH = '{0}/{1}'.format(APP_ROOT, '/server/tests')


@click.command()
@click.argument('path', default=TESTS_PATH)
def cli(path):
    """
    Run tests.

    :return: Subprocess call result
    """
    cmd = 'py.test {0}'.format(path)
    return subprocess.call(cmd, shell=True)
