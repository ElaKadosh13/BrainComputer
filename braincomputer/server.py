import struct
import pathlib
import threading
from datetime import datetime
from .utils import Listener
from .utils import Connection

##### NOTES #####
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) to avoid annoying "port is already in use" errors.
# socket.recv() doesn't guarantee all the data will be received. so my_recvall loops until all data passed
# struct.unpack(buffer) Unpack from the buffer (presumably packed by pack(format, ...)) according to the complied format
# Handler class - gets a connection as a new thread, and 'start' invokes run
# path.mkdir(exists_ok=True, parents=True) - Create a new directory at this given path, If parents is true, any missing parents of this path are created as needed, If exist_ok is true, FileExistsError exceptions will be ignored
################

def run_server(address, data):
    print("in runserver")
    tuple_address = address.split(":")
    with Listener(int(tuple_address[1]), tuple_address[0]) as listener:
        while True:
            print("in forever loop")
            connection = listener.accept()
            print("fff")
            handler = Handler(connection, data)
            handler.start()

lock = threading.Lock()

class Handler(threading.Thread):

    def __init__(self, connection: Connection, data_dir):
        super().__init__()
        self.connection = connection
        self.data_root = pathlib.Path(data_dir)

    def run(self):
        struct_obj = struct.Struct('LLI')
        message_protocol = self.connection.receive(struct_obj.size)
        user_id, timestamp, thought_size = struct_obj.unpack(message_protocol)
        thought_data = self.connection.receive(thought_size).decode(encoding='utf-8')
        directory_path = self.data_root / str(user_id)
        file_name = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d_%H-%M-%S.txt')
        file_path = directory_path / file_name
        lock.acquire()
        try:
            directory_path.mkdir(parents=True, exist_ok=True)
            if file_path.exists():
                with file_path.open('a') as f:
                    f.write(f'\n{thought_data}')
            else:
                with file_path.open('w') as f:
                    f.write(f'{thought_data}')
        finally:
            lock.release()


if __name__ == '__main__':
    import sys
    sys.exit()




