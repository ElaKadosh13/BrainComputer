import sys
import click
import braincomputer
from braincomputer.client.client import upload_snapshots
from braincomputer.utils.log import log


@click.group()
@click.version_option(braincomputer.version)
@click.option('-q', '--quiet', is_flag=True)
@click.option('-t', '--traceback', is_flag=True)
def main(quiet=False, traceback=False):
    log.quiet = quiet
    log.traceback = traceback


@main.command("upload-snapshots", short_help="upload client thought")
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=8000)
@click.argument("path", type=str)
def run_c(host, port, path):
    address = host + ':' + str(port)
    log(upload_snapshots(address, path))


if __name__ == '__main__':
    try:
        main(prog_name='braincomputer', obj={})
    except Exception as error:
        log(f'ERROR: {error}')
        sys.exit(1)
