import sys
import click
import braincomputer
from braincomputer.utils.log import log
from braincomputer.saver.saver import run_saver


@click.group()
@click.version_option(braincomputer.version)
@click.option('-q', '--quiet', is_flag=True)
@click.option('-t', '--traceback', is_flag=True)
def main(quiet=False, traceback=False):
    log.quiet = quiet
    log.traceback = traceback

@main.command("run-saver", short_help="run saver")
def run_sa():
    log(run_saver())

if __name__ == '__main__':
    try:
        main(prog_name='braincomputer', obj={})
    except Exception as error:
        log(f'ERROR: {error}')
        sys.exit(1)
