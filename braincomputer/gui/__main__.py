import sys
import click
import braincomputer
from braincomputer.utils.log import log


@click.group()
@click.version_option(braincomputer.version)
@click.option('-q', '--quiet', is_flag=True)
@click.option('-t', '--traceback', is_flag=True)
def main(quiet=False, traceback=False):
    log.quiet = quiet
    log.traceback = traceback

@main.command("run-webserver", short_help="run webserver forever")
@click.argument("address", type=str)
@click.argument("data_dir", type=str)
def run_ws(address, data_dir):
    log(run_webserver(address, data_dir))


if __name__ == '__main__':
    try:
        main(prog_name='braincomputer', obj={})
    except Exception as error:
        log(f'ERROR: {error}')
        sys.exit(1)
