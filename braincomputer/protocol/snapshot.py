import struct
import io
from braincomputer.utils.image import ColorImage, DepthImage


class Snapshot:
    def __init__(self, datetime, translation=(0, 0, 0), rotation=(0, 0, 0, 0),
                 color_image=None, depth_image=DepthImage(0, 0, []),
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
        color_image_width = color_image_height = depth_image_width = depth_image_height = 0
        color_image_data = b''
        depth_image_data = []

        if "color_image" in config.fields:
            color_image_height = self.color_image.height
            color_image_width = self.color_image.width
            color_image_data = self.color_image.image_data

        if "depth_image" in config.fields:
            depth_image_height = self.depth_image.height
            depth_image_width =  self.depth_image.width
            depth_image_data = self.depth_image.image_data

        color_image_size = len(color_image_data)
        depth_image_size = len(depth_image_data)
        serialized_snapshot = struct.pack(f'<QdddddddII{color_image_size}sII{depth_image_size}fffff',
                                          self.datetime, *self.translation, *self.rotation,
                                          color_image_height, color_image_width, color_image_data,
                                          depth_image_height, depth_image_width, *depth_image_data,
                                          *self.user_feelings)
        return serialized_snapshot

    @classmethod
    def deserialize(cls, serialized_data):
        stream_data = SerializedDataStream(io.BytesIO(serialized_data))
        timestamp = stream_data.deserialize('Q')
        translation = stream_data.deserialize('ddd')
        rotation = stream_data.deserialize('dddd')

        color_image_height, = stream_data.deserialize('I')
        color_image_width, = stream_data.deserialize('I')
        color_image_size = color_image_height * color_image_width * 3
        color_image_data = stream_data.deserialize(f'{color_image_size}s')
        color_image = ColorImage(color_image_width, color_image_height, color_image_data[0])

        depth_image_height, = stream_data.deserialize('I')
        depth_image_width, = stream_data.deserialize('I')
        depth_image_size = depth_image_height * depth_image_width
        depth_image_data = stream_data.deserialize(f'{depth_image_size}f')
        depth_image = DepthImage(depth_image_width, depth_image_height, depth_image_data)

        user_feelings = stream_data.deserialize('ffff')

        return Snapshot(timestamp, translation, rotation, color_image, depth_image, user_feelings)


class SerializedDataStream:
    def __init__(self, serialized_data_stream):
        self.serialized_data_stream = serialized_data_stream
        
    def deserialize(self, by_format):
        return struct.unpack(by_format, self.serialized_data_stream.read(struct.calcsize(by_format)))
