from braincomputer.client import upload_sample
import socket
import threading
from braincomputer.utils.reader import Reader
from braincomputer.utils.connection import Connection
from braincomputer.utils.user import User
from braincomputer.protocol import Hello, Config, Snapshot
from braincomputer.utils.image import ColorImage, DepthImage


def mock_reader_init(self, path):
    self.user = User(1, "ela", 111111, "f")
    self.snapshots = mock_iterate_snapshot(0)


def mock_iterate_snapshot(y):
    while y < 1:
        y = 1
        yield Snapshot(111, (1, 2, 3), (1, 2, 3, 4),
                 color_image=ColorImage(0, 0, b''), depth_image=DepthImage(0, 0, b''),
                 user_feelings=(1, 2, 3, 4))


def mock_server(host, port):
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen()
    sock.accept()


def mock_connection_recv(self):
    config = ["feelings", "pose", "color_image", "depth_image"]
    return Config(len(config), config).serialize()


def test_upload_snapshot(monkeypatch, capsys):
    monkeypatch.setattr(Reader, "__init__", value=mock_reader_init)
    monkeypatch.setattr(Connection, "receive_message", value=mock_connection_recv)
    host = '127.0.0.1'
    port = 8001
    server = threading.Thread(target=mock_server, args=(host, port))
    server.start()
    upload_sample(host, port, '../sample/snapshot.txt')
    c = capsys.readouterr()
    assert "client running- may take some time" in c.out
    assert "client done" in c.out

