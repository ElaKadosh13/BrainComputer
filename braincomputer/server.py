import pathlib
import threading
from datetime import datetime

from braincomputer.parsers import Parsers
from braincomputer.protocol import Hello, Config, Snapshot
from .utils import Listener


def run_server(address, data):
    tuple_address = address.split(":")
    parsers = Parsers()  # init parsers
    with Listener(int(tuple_address[1]), tuple_address[0]) as listener:
        while True:
            connection = listener.accept()
            handler = Handler(connection, data, parsers)
            handler.start()


class Context:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        Handler.lock.acquire()
        try:
            self.data_dir.mkdir(parents=True, exist_ok=True)
        finally:
            Handler.lock.release()

    def save(self, parser_name, data):
        Handler.lock.acquire()
        try:
            file_path = self.data_dir / parser_name
            mode = 'w'
            if file_path.exists():
                mode = 'a'
            with file_path.open(mode) as f:
                f.write(data)
        finally:
            Handler.lock.release()


class Handler(threading.Thread):
    lock = threading.Lock()

    def __init__(self, connection, data_dir, parsers):
        super().__init__()
        self.connection = connection
        self.data_root = pathlib.Path(data_dir)
        self.parsers = parsers

    def run(self):
        print("server running")
        # receive hello
        deserialized_hello = Hello.deserialize(self.connection.receive_message())
        # send config
        config_fields = self.parsers.parsers_functions.keys()
        serialized_config = Config(len(config_fields), config_fields).serialize()
        self.connection.send_message(serialized_config)
        # receive snapshot
        deserialized_snapshot = Snapshot.deserialize(self.connection.receive_message())
        # handle files
        directory_path = self.data_root / str(deserialized_hello.user_id)
        print(deserialized_snapshot.datetime)
        dt = deserialized_snapshot.datetime  # /1000 to miliseconds
        dattime = datetime.fromtimestamp(dt / 1000).strftime(
            '%Y-%m-%d_%H-%M-%S-%f')  # todo - make sure the ts is ok by the format
        directory = directory_path / dattime
        # handle parsers
        client_context = Context(directory)
        self.parsers.parse(client_context, deserialized_snapshot)


if __name__ == '__main__':
    import sys

    sys.exit()
