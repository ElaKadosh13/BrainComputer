import socket


class Connection:

    def __init__(self, sock):
        self.sock = sock

    def __repr__(self):
        from_port = self.sock.getsockname()[1]
        to_port = self.sock.getpeername()[1]
        return f'<Connection from 127.0.0.1:{from_port}' \
               f' to 127.0.0.1:{to_port}>'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()

    def send(self, data):
        self.sock.sendall(data)

    def receive(self, size):
        current_bytes = self.sock.recv(size)
        if len(current_bytes) < size:
            buffer = [current_bytes]
            recv_so_far = len(current_bytes)
            while recv_so_far < size:
                left_size = size - recv_so_far
                current_bytes = self.sock.recv(left_size)
                if len(current_bytes) == 0:
                    raise RuntimeError("data is incomplete")
                buffer.append(current_bytes)
                recv_so_far = recv_so_far + len(current_bytes)
            return b''.join(buffer)
        return current_bytes

    @classmethod
    def connect(cls, host, port):
        sock = socket.socket()
        sock.connect((host, port))
        return Connection(sock)
