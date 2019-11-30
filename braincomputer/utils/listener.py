import socket

from braincomputer.utils import Connection


class Listener:
    def __init__(self, port, host='0.0.0.0', backlog=1000, reuseaddr=True):
        self.port = port
        self.host = host
        self.backlog = backlog
        self.reuseaddr = reuseaddr
        self.socket = socket.socket()

    def __repr__(self):
        return f'Listener(port={self.port!r}, host={self.host!r}, backlog={self.backlog!r}, reuseaddr={self.reuseaddr!r})'

    def __enter__(self):
        if self.reuseaddr:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        address = (self.host, self.port)
        self.socket.bind(address)
        self.socket.listen(self.backlog)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.socket.close()

    def accept(self):
        connection = self.socket.accept()[0]
        return Connection(connection)