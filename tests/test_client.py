from braincomputer.client import upload_sample
import socket
import threading

from braincomputer.proto.messages_pb2 import User, Snapshot
from braincomputer.utils.reader import Reader


def mock_reader_init(self, path):
    self.user = User().ParseFromString(b'\x08*\x12\nEla Kadosh\x18\xe0\x90\xd5\xcd\x02')

#todo - run a snapshot
def mock_reader_iter(self):
    #snapshot = Snapshot().ParseFromString(b'\x08*\x12\neeeee\x18\xe0\x90\xd5\xcd\x02')
    #return iter(list(snapshot))
    return iter("")

def mock_server(host, port):
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen()
    sock.accept()
    sock.close()


def test_upload_snapshot(monkeypatch, capsys):
    monkeypatch.setattr(Reader, "__init__", value=mock_reader_init)
    monkeypatch.setattr(Reader, "__iter__", value=mock_reader_iter)
    host = '127.0.0.1'
    port = 8000
    server = threading.Thread(target=mock_server, args=(host, port))
    server.start()
    upload_sample(host, port, '../sample/snapshot.txt')
    c = capsys.readouterr()
    assert "client running- may take some time" in c.out
    assert "client done" in c.out

