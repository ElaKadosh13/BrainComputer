import matplotlib.cm
import numpy
import matplotlib.pyplot


def parse_depth_image(context, snapshot):
    image = numpy.array(snapshot.depth_image.image_data).reshape((snapshot.depth_image.height, snapshot.depth_image.width))
    file_path = context.data_dir / "depth_image.jpg"
    matplotlib.pyplot.imsave(file_path, image)


parse_depth_image.field = 'depth_image'
