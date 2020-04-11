from braincomputer.parsers.parsers import parse
import cv2


def test_parser_pose(capsys):
    parse('pose', 'tests/sources/raw_data.txt')
    c = capsys.readouterr()
    assert """"translation": [0.4873843491077423, 0.007090016733855009, -1.1306129693984985]""" in c.out
    assert """"rotation": [-0.10888676356214629, -0.26755994585035286, -0.021271118915446748, 0.9571326384559261]""" in c.out


def test_parser_feelings(capsys):
    parse('feelings', 'tests/sources/raw_data.txt')
    c = capsys.readouterr()
    assert """feelings": [0.0, 0.0, 0.0, 0.0]""" in c.out


def test_parser_color_image(capsys):
    parse('color_image', 'tests/sources/raw_data.txt')
    c = capsys.readouterr()
    assert """"color_image": [1920, 1080, "tests/sources/42_2019-12-04_10-08-07-339000_color_image_data.jpg"]}""" in c.out
    assert check_images_equality("tests/sources/expected_color_image_data.jpg", "tests/sources/42_2019-12-04_10-08-07-339000_color_image_data.jpg") == True


def test_parser_depth_image(capsys):
    parse('depth_image', 'tests/sources/raw_data.txt')
    c = capsys.readouterr()
    assert """depth_image": [224, 172, "tests/sources/42_2019-12-04_10-08-07-339000_depth_image_data.jpg"]}""" in c.out
    assert check_images_equality("tests/sources/expected_depth_image_data.jpg", "tests/sources/42_2019-12-04_10-08-07-339000_depth_image_data.jpg") == True


def check_images_equality(expected, result):
    e = cv2.imread(expected)
    r = cv2.imread(result)
    if e.shape != r.shape:
        return False
    diff = cv2.subtract(e, r)
    b, g, r = cv2.split(diff)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        return True
    return False
