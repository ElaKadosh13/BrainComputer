
class Image:
    def __init__(self, width=0, height=0, image_data=None):
        self.width = width
        self.height = height
        self.image_data = image_data

    def is_empty(self):
        return self.image_data is None


class ColorImage(Image):
    def __repr__(self):
        return f'ColorImage(width={self.width}, height={self.height})'


class DepthImage(Image):
    def __repr__(self):
        return f'DepthImage(width={self.width}, height={self.height})'

