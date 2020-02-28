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
        print("@@@@@@@@@@@@@@@")
        fields = config.fields
        if 'translation' in fields:
            translation = self.translation
        else:
            translation = (0, 0, 0)
        if 'rotation' in fields:
            rotation = self.rotation
        else:
            rotation = (0, 0, 0, 0)
        feelings = self.user_feelings if 'feelings' in fields else (0, 0, 0, 0)
        if 'color_image' in fields:
            w=self.color_image.width
            h=self.color_image.height
            data = self.color_image.image_data
        else:
            w=0
            h=0
            data=b''

        if 'depth_image' in fields:
            d_w=self.depth_image.width
            d_h=self.depth_image.height
            d_data = self.depth_image.image_data
        else:
            d_w =0
            d_h =0
            d_data=[]

        print("###############")
        params = [self.datetime, *translation, *rotation, h, w]
        if data:
            params.append(data)
        params.extend([d_w, d_h])
        params.extend(d_data)
        print("!!!!!!!!!!!!!!")
        return struct.pack(f'<QdddddddII{len(data)}sII{len(d_data)}fffff',
                           *params, *feelings)
        #config_fields = config.fields
        #serialized_snapshot = [struct.pack('Q', self.datetime)]
        #if "translation" in config_fields:
        #    serialized_snapshot.append(struct.pack('ddd', *self.translation))
        #else:
        #    serialized_snapshot.append(struct.pack('ddd', *(0, 0, 0)))
        #if "rotation" in config_fields:
        #    serialized_snapshot.append(struct.pack('dddd', *self.rotation))
        #else:
        #    serialized_snapshot.append(struct.pack('dddd', *(0, 0, 0, 0)))
        #if "feelings" in config_fields:
        #    serialized_snapshot.append(struct.pack('ffff', *self.user_feelings))
        #else:
        #    serialized_snapshot.append(struct.pack('ffff', *(0, 0, 0, 0)))
        #if "color_image" in config_fields:
        #    serialized_snapshot.append(self.color_image.serialize())
        #else:
        #    serialized_snapshot.append(ColorImage(0, 0, None).serialize())
        #if "depth_image" in config_fields:
        #     print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
        #     serialized_snapshot.append(self.depth_image.serialize())
        #else:
        #    print("depth image none")
        #    serialized_snapshot.append(DepthImage(0, 0, None).serialize())
        #return b''.join(serialized_snapshot)

    @classmethod
    def deserialize(cls, serialized_data):

        #stream_data = io.BytesIO(serialized_data)
        #timestamp = struct.unpack('Q', stream_data.read(8))
        #translation = struct.unpack('ddd', stream_data.read(24))
        #rotation = struct.unpack('dddd', stream_data.read(32))
        #user_feelings = struct.unpack('ffff', stream_data.read(16))
        #color_image = ColorImage.deserialize(stream_data)
        #print("depth image deserialize")
        #depth_image = DepthImage.deserialize(stream_data)
        #print("depth image deserialize 2")
        #return Snapshot(timestamp, translation, rotation, color_image, depth_image, user_feelings)
        stream_data = io.BytesIO(serialized_data)
        timestamp, translation_x, translation_y, translation_z, \
        rotation_x, rotation_y, rotation_z, rotation_w, \
        height, width = binary_from_stream(stream_data, 'QdddddddII')
        pixels = None
        #if 'color_image' in fields:
        pixels = binary_from_stream(stream_data, f'{3 * height * width}s')[0]
        depth_height, depth_width = binary_from_stream(stream_data, 'II')

        depth_pixels = None
        #if 'depth_image' in fields:
        depth_pixels = binary_from_stream(stream_data, f'{depth_height * depth_width}f')

        hunger, thirst, exhaustion, happiness = binary_from_stream(stream_data, 'ffff')

        return Snapshot(timestamp, (translation_x, translation_y, translation_z),
                        (rotation_x, rotation_y, rotation_z, rotation_w),
                        ColorImage(width, height, pixels),
                        DepthImage(depth_width, depth_height, depth_pixels),
                        (hunger, thirst, exhaustion, happiness))


def binary_from_stream(stream, struct_format):
    size = struct.calcsize(struct_format)
    print("size")
    print(size)
    buf = stream.read(size)
    if buf is None:
        return None
    print("bfsssssss")
    res = struct.unpack(struct_format, buf)
    return res