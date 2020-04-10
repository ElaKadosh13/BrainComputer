import time

from braincomputer.protocol import Hello, Config
from braincomputer.utils import Connection
from braincomputer.utils.reader import Reader


def upload_sample(host, port, path):
    print("client running- may take some time")
    reader = Reader(path)
    for snapshot in reader:
        time.sleep(0.5)
        with Connection.connect(host, int(port)) as connection:
            # send hello
            connection.send_message(Hello(reader.user.user_id, reader.user.user_name,
                                    reader.user.user_birthday, reader.user.user_gender).serialize())
            # receive config
            c = connection.receive_message()
            deserialized_config = Config.deserialize(c)
            # send snapshot
            serialized_snapshot = snapshot.serialize(deserialized_config)
            connection.send_message(serialized_snapshot)
    print("client done")
