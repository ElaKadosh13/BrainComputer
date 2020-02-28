import struct


class Image:
    def __init__(self, width=0, height=0, image_data=None):
        self.width = width
        self.height = height
        self.image_data = image_data

    def is_empty(self):
        return self.image_data is None

# todo - move serialize to image if possible


class ColorImage(Image):
    def __repr__(self):
        return f'ColorImage(width={self.width}, height={self.height})'

    def serialize(self):
        if self.is_empty():
            return b''.join([struct.pack('II', *(0, 0))])
        d = [struct.pack('I', self.width), struct.pack('I', self.height), self.image_data]
        print("bbbbbbbb")
        print(type(d))
        return b''.join(d)

    @classmethod
    def deserialize(cls, serialized_data):
        width, = struct.unpack('I', serialized_data.read(4))
        height, = struct.unpack('I', serialized_data.read(4))
        if width != 0 and height != 0:
            image_data = serialized_data.read(width * height * 3)  # rgb triplet for each pixel
        else:
            image_data = None
        return ColorImage(width, height, image_data)


class DepthImage(Image):
    def __repr__(self):
        return f'DepthImage(width={self.width}, height={self.height})'

    def serialize(self):
        print("serialize depth image")
        if self.is_empty():
            return b''.join([struct.pack('sII', *(0, 0, 0))])
        d = [struct.pack('I', self.width), struct.pack('I', self.height), self.image_data]
        print("non empty depth image")
        print("aaaaaaa")
        print(type(d))
        x = b''.join(d)
        print("ddddddddddddddddddddddddd")
        return x

    @classmethod
    def deserialize(cls, serialized_data):
        width, = struct.unpack('I', serialized_data.read(4))
        height, = struct.unpack('I', serialized_data.read(4))  # 4 byte int
        if width != 0 and height != 0:
            image_data = serialized_data.read(width * height * 4)  # float for each pixel
        else:
            image_data = None
        return DepthImage(width, height, image_data)
