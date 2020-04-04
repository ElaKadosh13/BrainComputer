import sys
import click
import braincomputer
from braincomputer.api.api import run_api_server
from braincomputer.utils.log import log


@click.group()
@click.version_option(braincomputer.version)
@click.option('-q', '--quiet', is_flag=True)
@click.option('-t', '--traceback', is_flag=True)
def main(quiet=False, traceback=False):
    log.quiet = quiet
    log.traceback = traceback


@main.command("run-server", short_help="run webserver forever")
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=8080)
@click.option('-d', '--database', default='mongodb://127.0.0.1:27017')
def run_ws(host, port, database):
    log(run_api_server(host, port, database))


if __name__ == '__main__':
    try:
        main(prog_name='braincomputer', obj={})
    except Exception as error:
        log(f'ERROR: {error}')
        sys.exit(1)
