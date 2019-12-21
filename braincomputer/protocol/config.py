import struct
import io


class Config:
    def __init__(self, number_of_fields, fields):
        self.number_of_fields = number_of_fields
        self.fields = fields

    def __repr__(self):
        return f'Config(number_of_fields={self.number_of_fields}, fields={self.fields})'

    def serialize(self):
        serialized = [struct.pack('I', self.number_of_fields)]
        for f in self.fields:
            serialized.append(struct.pack('I', len(f)))
            serialized.append(f.encode('utf-8'))
        return b''.join(serialized)

    @classmethod
    def deserialize(cls, serialized_data):
        stream_data = io.BytesIO(serialized_data)
        number_of_fields, = struct.unpack('I', stream_data.read(4))  # int - 4 bytes
        fields = []
        for f in range(number_of_fields):
            f_len, = struct.unpack('I', stream_data.read(4))
            fields.append(stream_data.read(f_len).decode('utf-8'))
        return Config(number_of_fields, fields)

