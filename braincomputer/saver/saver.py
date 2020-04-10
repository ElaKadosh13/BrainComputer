import pika

from braincomputer.db import Db
from braincomputer.mq.mq import Mq


class Saver:
    def __init__(self, db_url):
        self.db = Db(db_url)
        print("created db")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close_db()

    def save(self, parser_type, data):
        self.db.save_to_db(data)

    def callback(self, ch, method, properties, body):
        print("in callback, saver data:")
        self.save(method.routing_key, body)

    def handle_queue(self, mq_url):
        mq = Mq(mq_url)
        print("cerated mq")
        queue_name = 'parsed'
        mq.create_queue(queue_name, 'topic')
        print("created queue, consuming")
        parser_keys = ['pose', 'feelings', 'color_image', 'depth_image']
        mq.consume_from_queue(queue_name, self.callback, parser_keys)


def run_saver(mq_url, db_url):
    with Saver(db_url) as saver:
        print('saving...')
        saver.handle_queue(mq_url)


def save(db_url, parser_type, path):
    print("in save")
    with Db(db_url) as db:
        with open(path, 'r') as f:
            data = f.read()
        db.save_to_db(data)
