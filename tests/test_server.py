from braincomputer.client import upload_sample
from braincomputer.server import run_server
import json
import threading
from braincomputer.utils.reader import Reader
from braincomputer.utils.connection import Connection
from braincomputer.utils.user import User
from braincomputer.protocol import Hello, Config, Snapshot
from braincomputer.utils.image import ColorImage, DepthImage

user = User(1, "ela", 699746400, "f")
hello = Hello(user.user_id, user.user_name, user.user_birthday, user.user_gender)
config = Config(4, ["feelings", "pose", "color_image", "depth_image"])
snapshot = Snapshot(1575446887339, (1, 2, 3), (1, 2, 3, 4),
                        color_image=ColorImage(0, 0, b''), depth_image=DepthImage(0, 0, b''),
                        user_feelings=(1, 2, 3, 4))


def mock_client_send_hello(connection):
    connection.send(hello.serialize())


def mock_client_send_snapshot(connection):
    connection.send(snapshot.serialize(config))


def mock_hello_deserialize(hello_ser):
    return hello


def mock_snapshot_deserialize(snapshot_ser):
    return snapshot


def mock_receive_message(self):
    pass


def mock_to_json(self, root, userr, dt):
    return json.dumps({
            'user': {'id': user.user_id, 'name': user.user_name, 'birthday': user.user_birthday, 'gender': user.user_gender},
            'timestamp': [snapshot.datetime],
            'translation': snapshot.translation,
            'rotation': snapshot.rotation,
            'color_image': {'width': snapshot.color_image.width, 'height': snapshot.color_image.height,
                            'path': snapshot.color_image.path_to_data},
            'depth_image': {'width': snapshot.depth_image.width, 'height': snapshot.depth_image.height,
                            'path': snapshot.depth_image.path_to_data},
            'feelings': snapshot.user_feelings
        })


def print_message(message):
    print(message)


def test_run_server(monkeypatch, capsys):
    monkeypatch.setattr(Hello, "deserialize", value=mock_hello_deserialize)
    monkeypatch.setattr(Snapshot, "deserialize", value=mock_snapshot_deserialize)
    monkeypatch.setattr(Snapshot, "to_json", value=mock_to_json)
    monkeypatch.setattr(Connection, "receive_message", value=mock_receive_message)
    host = '127.0.0.1'
    port = 8003
    server = threading.Thread(target=run_server, args=(host, port, print_message))
    server.daemon = True
    server.start()
    import time
    time.sleep(0.1)
    with Connection.connect(host, port) as connection:
        mock_client_send_hello(connection)
        time.sleep(0.1)
        mock_client_send_snapshot(connection)
        time.sleep(0.1)
    c, err = capsys.readouterr()
    publish = """{"user": {"id": 1, "name": "ela", "birthday": 699746400, "gender": "f"}, "timestamp": [1575446887339], "translation": [1, 2, 3], "rotation": [1, 2, 3, 4], "color_image": {"width": 0, "height": 0, "path": ""}, "depth_image": {"width": 0, "height": 0, "path": ""}, "feelings": [1, 2, 3, 4]}\n"""
    assert c == publish
    assert err == ''




