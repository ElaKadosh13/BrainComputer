import threading
from braincomputer.protocol import Hello, Config, Snapshot
from braincomputer.utils import Listener

lock = threading.Lock()


def handle_client(connection, data, publish):
    handler = Handler(connection, data, publish)
    handler.start()


def run_server(host, port, publish):
    data_dir = "braincomputer/gui/static/"
    with Listener(int(port), host) as listener:
        while True:
            connection = listener.accept()
            threading.Thread(target=handle_client, args=(connection, data_dir, publish)).start()


class Handler(threading.Thread):
    def __init__(self, connection, data_dir, publish):
        super().__init__()
        self.connection = connection
        self.data_root = data_dir
        self.publish = publish

    def run(self):
        # receive hello
        deserialized_hello = Hello.deserialize(self.connection.receive_message())
        # send config
        config_fields = ["feelings", "pose", "color_image", "depth_image"]
        serialized_config = Config(len(config_fields), config_fields).serialize()
        self.connection.send_message(serialized_config)
        # receive snapshot
        deserialized_snapshot = Snapshot.deserialize(self.connection.receive_message())
        # push to message queue
        lock.acquire()
        try:
            json_snapshot = deserialized_snapshot.to_json(self.data_root,
                                                          deserialized_hello,
                                                          deserialized_snapshot.datetime[0])
            self.publish(json_snapshot)
        except:
            raise Exception("Server failed to publish the snapshot to mq")
        finally:
            lock.release()


if __name__ == '__main__':
    import sys

    sys.exit()
