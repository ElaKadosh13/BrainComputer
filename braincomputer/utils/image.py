import struct


class Image:
    def __init__(self, width=0, height=0, image_data=None):
        self.width = width
        self.height = height
        self.image_data = image_data

    def is_empty(self):
        return self.image_data is None

    def serialize(self):
        if self.is_empty:
            return b''
        d = [struct.pack('I', self.width), struct.pack('I', self.height), self.image_data]
        print(d)
        return b''.join(d)


class ColorImage(Image):
    def __repr__(self):
        return f'ColorImage(width={self.width}, height={self.height})'

    @classmethod
    def deserialize(cls, serialized_data):
        print("image deserialize")
        print(serialized_data)
        width, = struct.unpack('I', serialized_data.read(4))
        height, = struct.unpack('I', serialized_data.read(4))
        image_data = serialized_data.read(width * height * 3)  # rgb triplet for each pixel
        return ColorImage(width, height, image_data)


class DepthImage(Image):
    def __repr__(self):
        return f'DepthImage(width={self.width}, height={self.height})'

    @classmethod
    def deserialize(cls, serialized_data):
        width, = struct.unpack('I', serialized_data.read(4))
        height, = struct.unpack('I', serialized_data.read(4))  # 4 byte int
        image_data = serialized_data.read(width * height * 4)  # float for each pixel
        return DepthImage(width, height, image_data)
