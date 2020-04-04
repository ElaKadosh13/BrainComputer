import time

from braincomputer.protocol import Hello, Config
from braincomputer.utils import Connection
from braincomputer.utils.reader import Reader

def upload_sample(host, port, path):
    print("in client")
    reader = Reader(path)
    for snapshot in reader:
        time.sleep(1)  # todo - maybe not necessary??
        address = host + ':' + str(port) #todo - refactor those 2 dumb lies
        tuple_address = address.split(":")
        with Connection.connect(tuple_address[0], int(tuple_address[1])) as connection:
            print("in client - snapshot")
            # send hello
            connection.send_message(Hello(reader.user.user_id, reader.user.user_name,
                                  reader.user.user_birthday, reader.user.user_gender).serialize())
            # receive config
            c = connection.receive_message()
            deserialized_config = Config.deserialize(c)
            # send snapshot
            serialized_snapshot = snapshot.serialize(deserialized_config)
            connection.send_message(serialized_snapshot)
