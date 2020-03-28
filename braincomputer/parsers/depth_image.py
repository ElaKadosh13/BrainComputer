import matplotlib.cm
import numpy
import matplotlib.pyplot
import json
import pathlib
import struct


def parse_depth_image(snapshot):
    data = json.loads(snapshot)
    depth_image = data['depth_image']
    depth_image_height = depth_image['height']
    depth_image_width = depth_image['width']
    depth_image_path = depth_image['path']
    depth_image_data_path = pathlib.Path(depth_image_path)
    image_size = depth_image_width * depth_image_height
    image_data_format = f'{image_size}f'
    with depth_image_data_path.open('rb') as f:
        image_data_packed = f.read(struct.calcsize(image_data_format))
    image_data = struct.unpack(image_data_format, image_data_packed)
    image = numpy.array(image_data).reshape((depth_image_height, depth_image_width))
    image_path = depth_image_path + ".jpg"
    matplotlib.pyplot.imsave(image_path, image)
    return json.dumps({'user': data['user'],
                       'ts': data['timestamp'],
                       "depth_image": [depth_image_width, depth_image_height, image_path]})


parse_depth_image.field = 'depth_image'
