import time

from braincomputer.protocol import Hello, Config
from braincomputer.utils import Connection
from braincomputer.utils.reader import Reader


def upload_snapshots(address, file_path):
    reader = Reader(file_path)
    for snapshot in reader:
        time.sleep(0.5)  # todo - maybe not necessary??
        tuple_address = address.split(":")
        with Connection.connect(tuple_address[0], int(tuple_address[1])) as connection:
            # send hello
            connection.send_message(Hello(reader.user.user_id, reader.user.user_name,
                                  reader.user.user_birthday, reader.user.user_gender).serialize())
            # receive config
            c = connection.receive_message()
            deserialized_config = Config.deserialize(c)
            # send snapshot
            connection.send_message(snapshot.serialize(deserialized_config))
