
import struct
import datetime
from datetime import datetime

struct_format = struct.Struct('LLI')

class Thought:
    def __init__(self, user_id, timestamp, thought):
       self.user_id = user_id
       self.timestamp = timestamp
       self.thought = thought

    def __repr__(self):
       return f'Thought(user_id={self.user_id!r}, timestamp={self.timestamp!r}, thought={self.thought!r})'

    def __str__(self):
        return f'[{self.timestamp}] user {self.user_id}: {self.thought}'

    def __eq__(self, other):
        if type(self) == type(other):
            if self.user_id == other.user_id and self.timestamp == other.timestamp and self.thought == other.thought:
                return True
        return False

    def serialize(self):
        fixed_timestamp = int(datetime.timestamp(self.timestamp))
        fixed_thought_length = len(self.thought)
        serialized_thought = bytes(self.thought, 'utf-8')
        return struct.pack('LLI', self.user_id, fixed_timestamp, fixed_thought_length) + serialized_thought

    @staticmethod
    def deserialize(data):
        structdata = data.split(b'\n')[0]
        thoughtdata = data.split(b'\n')[1][3:].decode()
        user_id, timestamp = struct.unpack('LL', structdata)
        return Thought(user_id, datetime.fromtimestamp(timestamp), thoughtdata)
