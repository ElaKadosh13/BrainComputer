import struct
import io
from braincomputer.utils.image import ColorImage, DepthImage


class Snapshot:
    def __init__(self, datetime, translation=(0, 0, 0), rotation=(0, 0, 0, 0),
                 color_image=None, depth_image=None,
                 user_feelings=(0, 0, 0, 0)):
        self.datetime = datetime
        self.translation = translation
        self.rotation = rotation
        self.color_image = color_image
        self.depth_image = depth_image
        self.user_feelings = user_feelings

    def __repr__(self):
        return f'Snapshot(datetime={self.datetime}, translation={self.translation}, rotation={self.rotation},' \
                    f'color_image={self.color_image}, depth_image={self.depth_image}, user_feelings={self.user_feelings})'

    def serialize(self, config):
        config_fields = config.fields
        serialized_snapshot = [struct.pack('Q', self.datetime)]
        if "translation" in config_fields:
            serialized_snapshot.append(struct.pack('ddd', *self.translation))
        else:
            serialized_snapshot.append(struct.pack('ddd', *(0, 0, 0)))
        if "rotation" in config_fields:
            serialized_snapshot.append(struct.pack('dddd', *self.rotation))
        else:
            serialized_snapshot.append(struct.pack('dddd', *(0, 0, 0, 0)))
        if "feelings" in config_fields:
            serialized_snapshot.append(struct.pack('ffff', *self.user_feelings))
        else:
            serialized_snapshot.append(struct.pack('ffff', *(0, 0, 0, 0)))
        if "color_image" in config_fields:
            serialized_snapshot.append(self.color_image.serialize())
        else:
            serialized_snapshot.append(ColorImage(0, 0, None).serialize())
        # if "depth_image" in config_fields:
        #     serialized_snapshot.append(self.depth_image.serialize())
        # else:
        #     serialized_snapshot.append(DepthImage(0, 0, None).serialize())
        return b''.join(serialized_snapshot)

    @classmethod
    def deserialize(cls, serialized_data):
        stream_data = io.BytesIO(serialized_data)
        timestamp = struct.unpack('Q', stream_data.read(8))
        translation = struct.unpack('ddd', stream_data.read(24))
        rotation = struct.unpack('dddd', stream_data.read(32))
        user_feelings = struct.unpack('ffff', stream_data.read(16))
        color_image = ColorImage.deserialize(stream_data)
        depth_image = None #DepthImage.deserialize(stream_data)
        return Snapshot(timestamp, translation, rotation, color_image, depth_image, user_feelings)
