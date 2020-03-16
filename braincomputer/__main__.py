import os
import sys
import traceback

import click
import braincomputer
from braincomputer import upload_snapshots, run_server, run_webserver
from braincomputer.parsers.parsers import run_parser
from braincomputer.saver.saver import run_saver
from braincomputer.utils.reader import start_reader


class Log:

    def __init__(self):
        self.quiet = False
        self.traceback = False

    def __call__(self, message):
        if self.quiet:
            return
        if self.traceback and sys.exc_info():  # there's an active exception
            message += os.linesep + traceback.format_exc().strip()
        click.echo(message)


log = Log()

@click.group()
@click.version_option(braincomputer.version)
@click.option('-q', '--quiet', is_flag=True)
@click.option('-t', '--traceback', is_flag=True)
def main(quiet=False, traceback=False):
    log.quiet = quiet
    log.traceback = traceback


@main.command("run-parser", short_help="run parser by type")
@click.argument("parser_type", type=str)
def run_p(parser_type):
    log(run_parser(parser_type))


@main.command("run-saver", short_help="run saver")
def run_sa():
    log(run_saver())


@main.command("upload-snapshots", short_help="upload client thought")
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=8000)
@click.argument("path", type=str)
def run_c(host, port, path):
    address = host + ':' + str(port)
    log(upload_snapshots(address, path))


@main.command("run-server", short_help="run server forever")
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=8000)
@click.argument("data_dir", type=str)
def run_s(host, port, data_dir):
    address = host+':'+str(port)
    log(run_server(address, data_dir))


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
