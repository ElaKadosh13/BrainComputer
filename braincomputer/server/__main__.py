import sys
import click
import braincomputer
from braincomputer.mq import Mq
from braincomputer.utils.log import log
from braincomputer.server.server import run_server


@click.group()
@click.version_option(braincomputer.version)
@click.option('-q', '--quiet', is_flag=True)
@click.option('-t', '--traceback', is_flag=True)
def main(quiet=False, traceback=False):
    log.quiet = quiet
    log.traceback = traceback


@main.command("run-server", short_help="run server forever")
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=8000)
@click.argument("publish", type=str)
def run_s(host, port, publish):
    with Mq(publish) as mq:
        mq.create_queue('queue', 'fanout')
        mq_publish = mq.send_to_queue
        log(run_server(host, port, mq_publish))



if __name__ == '__main__':
    try:
        main(prog_name='braincomputer', obj={})
    except Exception as error:
        log(f'ERROR: {error}')
        sys.exit(1)
