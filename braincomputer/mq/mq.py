import pika

from braincomputer.mq.rabbitmq import Rabbitmq


class Mq:
    """If you want to change the queue just change lines 13-15 to the new queue initialization.
    Make sure the queue implements the methods:
    1. create_queue - set up parameters, connect, anything that needs to be done before we can send/recieve from the queue
    2. consume_from_queue
    3. send_to_queue
    4. close queue
    Also - all functions use *args so it's easy to replace to a queue that has different arguments for those methods
    """
    def __init__(self, address):
        self.queue = None
        split_addr = address.replace("/", "").split(":")
        if len(split_addr) != 3:
            raise Exception("invalid url, need to be mq://host:port")
        if split_addr[0] == 'rabbitmq':
            host, port = split_addr[1:]
            self.queue = Rabbitmq(host, port)
        else:
            raise Exception("currently only rabbitmq is supported")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_queue()

    def create_queue(self, *args):
        self.queue.create_queue(*args)

    def consume_from_queue(self, *args):
        self.queue.consume_from_queue(*args)

    def send_to_queue(self, *args):
        self.queue.send_to_queue(*args)

    def close_queue(self):
        self.queue.close_queue()
