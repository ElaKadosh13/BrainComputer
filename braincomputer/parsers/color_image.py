from PIL import Image as PIL
import json
import pathlib


def parse_color_image(snapshot):
    data = json.loads(snapshot)
    color_image = data['color_image']
    color_image_width = color_image['width']
    color_image_height = color_image['height']
    color_image_data_path = color_image['path']
    data_path = pathlib.Path(color_image_data_path)
    with data_path.open('rb') as f:
        image_data = f.read()
    image = PIL.frombytes('RGB', (color_image_width, color_image['height']), image_data)
    color_image_path = color_image_data_path + ".jpg"
    image.save(color_image_path)
    return json.dumps({'user': data['user'],
                       'ts': data['timestamp'],
                       'width': color_image_width,
                       'height': color_image_height,
                        'path': color_image_path})


parse_color_image.field = 'color_image'
