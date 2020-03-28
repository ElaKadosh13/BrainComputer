import pika

from braincomputer.db import Db
from braincomputer.mq.mq import Mq


class Saver:
    def __init__(self, mq_url, db_url):
        self.mq = Mq(mq_url)
        print("cerated mq")
        self.db = Db(db_url)
        print("created db")

    def callback(self, ch, method, properties, body):
        print("in callback, saver data:")
        self.db.save_to_db(body)

    def handle_queue(self):
        queue_name = 'parsed'
        self.mq.create_queue(queue_name)
        print("created queue, consuming")
        self.mq.consume_queue(queue_name, self.callback)


def run_saver(mq_url, db_url):
    saver = Saver(mq_url, db_url)
    print('saving...')
    saver.handle_queue()

