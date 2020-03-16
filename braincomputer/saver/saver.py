import pika

from braincomputer.db import Db
from braincomputer.mq.mq import Mq


class Saver:
    def __init__(self):
        self.mq = Mq()
        self.db = Db()
        self.db.create_db()

    def callback(self, ch, method, properties, body):
        print("in callback, saver data:")
        print(body)
        self.db.save_to_db("translation", body)


    def handle_queue(self):
        queue_name = 'parsed'
        self.mq.create_queue(queue_name)
        self.mq.consume_queue(queue_name, self.callback)


def run_saver():
    saver = Saver()
    print('saving...')
    saver.handle_queue()

