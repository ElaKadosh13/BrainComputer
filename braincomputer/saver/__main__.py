import sys
import click
import braincomputer
from braincomputer.utils.log import log
from braincomputer.saver.saver import run_saver, save


@click.group()
@click.version_option(braincomputer.version)
@click.option('-q', '--quiet', is_flag=True)
@click.option('-t', '--traceback', is_flag=True)
def main(quiet=False, traceback=False):
    log.quiet = quiet
    log.traceback = traceback


@main.command("save", short_help="run saver")
@click.option('-d', '--database', default='mongodb://127.0.0.1:27017')
@click.argument("parser_type", type=str)
@click.argument("path", type=str)
def run_save(database, parser_type, path):
    log(save(database, parser_type, path))


@main.command("run-saver", short_help="run saver")
@click.argument("mq_url", type=str)
@click.argument("db_url", type=str)
def run_sa(mq_url, db_url):
    log(run_saver(mq_url, db_url))


if __name__ == '__main__':
    try:
        main(prog_name='braincomputer', obj={})
    except Exception as error:
        log(f'ERROR: {error}')
        sys.exit(1)
