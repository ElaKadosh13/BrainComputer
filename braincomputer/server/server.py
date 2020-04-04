import threading
from ..mq.mq import Mq
from braincomputer.protocol import Hello, Config, Snapshot
from braincomputer.utils import Listener

queue_name = 'queue'

lock = threading.Lock()


def handle_client(connection, data, mq):
    handler = Handler(connection, data, mq)
    handler.start()


def run_server(host, port, publish):

    data_dir = "braincomputer/gui/static/"
    print("starting server")
    address = host + ':' + str(port)
    tuple_address = address.split(":")#todo - those 2 lines are dumb. fix.
    mq = Mq(publish)

    mq.create_queue(queue_name)
    with Listener(int(tuple_address[1]), tuple_address[0]) as listener:
        while True:
            connection = listener.accept()
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("new connection")
            threading.Thread(target=handle_client, args=(connection, data_dir, mq)).start()


class Handler(threading.Thread):
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
        lock.acquire() #todo - instead of locking can use different mq channels
        print("sending to queue")
        try:
            json_snapshot = deserialized_snapshot.to_json(self.data_root,
                                                          deserialized_hello,
                                                          deserialized_snapshot.datetime[0])
            print("snapshot converted")
            self.mq.send_to_queue(queue_name, json_snapshot)
        finally:
            lock.release()


if __name__ == '__main__':
    import sys

    sys.exit()
