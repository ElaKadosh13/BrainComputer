from PIL import Image as PIL


def parse_color_image(context, snapshot):
    image = PIL.frombytes('RGB', (snapshot.color_image.width, snapshot.color_image.height), bytes(snapshot.color_image.image_data))
    file_path = context.data_dir / "color_image.jpg"
    image.save(file_path)


parse_color_image.field = 'color_image'
