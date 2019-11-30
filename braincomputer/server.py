import socket
import struct
import pathlib
from datetime import datetime
from braincomputer.cli import CommandLineInterface

cli = CommandLineInterface()

def my_recvall(connection, fullsize):
    current_bytes = connection.recv(fullsize)

    if len(current_bytes) < fullsize:
        buffer = [current_bytes]
        recv_so_far = len(current_bytes)
        while recv_so_far < fullsize:
            left_size = fullsize - recv_so_far
            current_bytes = connection.recv(left_size)
            if len(current_bytes) == 0:
                raise RuntimeError("data is incomplete")
            buffer.append(current_bytes)
            recv_so_far = recv_so_far + len(current_bytes)
        return b''.join(buffer)

    return current_bytes

@cli.command
def run_server(address, data):
    listener = socket.socket()
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tuple_address = address.split(":")
    arg_address = (tuple_address[0], int(tuple_address[1]))
    listener.bind(arg_address)
    listener.listen()
    while True:
        connection, addr = listener.accept()
        data_root = pathlib.Path(data)
        struct_obj = struct.Struct('LLI')
        message_protocol = my_recvall(connection, struct_obj.size)
        user_id, timestamp, thought_size = struct_obj.unpack(message_protocol)
        thought_data = my_recvall(connection, thought_size).decode(encoding='utf-8')
        directory_path = data_root / str(user_id)
        file_name = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d_%H-%M-%S.txt')
        file_path = directory_path / file_name
        try:
            directory_path.mkdir(parents=True, exist_ok=True)
            if file_path.exists():
                with file_path.open('a') as f:
                    f.write(f'\n{thought_data}')
            else:
                with file_path.open('w') as f:
                    f.write(f'{thought_data}')
        finally:
            connection.close()

if __name__ == '__main__':
    import sys
    cli.main()
    sys.exit()





