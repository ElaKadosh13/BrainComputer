import os
import sys
import traceback

import click
import braincomputer
from braincomputer.parsers.parsers import run_parser_mq, parse
from braincomputer.utils.log import log


@click.group()
@click.version_option(braincomputer.version)
@click.option('-q', '--quiet', is_flag=True)
@click.option('-t', '--traceback', is_flag=True)
def main(quiet=False, traceback=False):
    log.quiet = quiet
    log.traceback = traceback


@main.command("run-parser", short_help="run parser by type")
@click.argument("parser_type", type=str)
@click.argument("mq_url", type=str)
def run_pa(parser_type, mq_url):
    log(run_parser_mq(parser_type, mq_url))


@main.command("parse", short_help="run parser by type")
@click.argument("parser_type", type=str)
@click.argument("raw_data_path", type=str)
def run_p(parser_type, raw_data_path):
    log(parse(parser_type, raw_data_path))


if __name__ == '__main__':
    try:
        main(prog_name='braincomputer', obj={})
    except Exception as error:
        log(f'ERROR: {error}')
        sys.exit(1)
