import io
import datetime
import struct


class Hello:
    def __init__(self, user_id, user_name, user_birthday, user_gender):
        self.user_id = user_id
        self.user_name = user_name
        self.user_birthday = user_birthday
        self.user_gender = user_gender

    def __repr__(self):
        return f'Hello(user_id={self.user_id}, user_name={self.user_name}, user_birthday={self.user_birthday},' \
               f' user_gender={self.user_gender})'

    def serialize(self):
        return b''.join([struct.pack('QI', self.user_id, len(self.user_name)), bytes(self.user_name, 'utf-8'),
                         struct.pack('Ic', self.user_birthday, bytes(self.user_gender[0], 'utf-8'))])

    @classmethod
    def deserialize(cls, serialized_data):
        stream_data = io.BytesIO(serialized_data)
        user_id, user_name_length = struct.unpack('QI', stream_data.read(8+4))  # int64 - 8 bytes
        user_name = stream_data.read(user_name_length).decode('utf-8')
        user_birthday, user_gender = struct.unpack('Ic', stream_data.read(4+1))
        user_gender = user_gender.decode('utf-8')
        return Hello(user_id, user_name, user_birthday, user_gender)

