import threading
from braincomputer.mq import Mq
from braincomputer.protocol import Hello, Config, Snapshot
from .utils import Listener

queue_name = 'queue'


def run_server(address, data):
    print("starting server")
    tuple_address = address.split(":")
    mq = Mq()

    mq.create_queue(queue_name,'5672')
    with Listener(int(tuple_address[1]), tuple_address[0]) as listener:
        while True:
            connection = listener.accept()
            handler = Handler(connection, data, mq)
            handler.start()


class Handler(threading.Thread):
    lock = threading.Lock()

    def __init__(self, connection, data_dir, mq):
        super().__init__()
        self.connection = connection
        self.data_root = data_dir
        self.mq = mq

    def run(self):
        print("server running")
        # receive hello
        deserialized_hello = Hello.deserialize(self.connection.receive_message())
        print(deserialized_hello)
        # send config
        config_fields = ["feelings", "pose", "color_image", "depth_image"] #todo -fix config? #self.parsers.parsers_functions.keys()
        serialized_config = Config(len(config_fields), config_fields).serialize()
        self.connection.send_message(serialized_config)
        # receive snapshot
        deserialized_snapshot = Snapshot.deserialize(self.connection.receive_message())
        # push to message queue
        Handler.lock.acquire()
        print("sending to queue")
        try:
            json_snapshot = deserialized_snapshot.to_json(self.data_root,
                                                          deserialized_hello,
                                                          deserialized_snapshot.datetime[0])
            self.mq.send_to_queue(queue_name, json_snapshot)
        finally:
            Handler.lock.release()


if __name__ == '__main__':
    import sys

    sys.exit()
