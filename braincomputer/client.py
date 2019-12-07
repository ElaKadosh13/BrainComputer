import datetime

from braincomputer.thought import Thought
from braincomputer.utils import Connection


def upload_thought(address, user_id, thought):
    tuple_address = address.split(":")
    with Connection.connect(tuple_address[0],
                            int(tuple_address[1])) \
            as connection:
        serialized_thought = Thought(user_id,
                                     datetime.datetime.now(),
                                     thought).serialize()
        connection.send(serialized_thought)
