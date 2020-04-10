import os
import pathlib
from datetime import datetime

from flask import Flask

from braincomputer.db import Db
from braincomputer.gui.html import _USER_LINE_HTML, _INDEX_HTML, _THOUGHT_LINE_HTML, _SNAPSHOT_HTML, _USERS_HTML, \
    _IMAGE_HTML, _FEELINGS_LINE_HTML, _FEELINGS_OVERTIME_HTML, _POSE_LINE_HTML, _POSE_OVERTIME_HTML, _IMAGE_LINE_HTML, \
    _IMAGE_OVERTIME_HTML

root_path = pathlib.Path(__file__).absolute().parent.parent
directory_path = ""
website = Flask(__name__)


def webserver_routers(db):
    @website.route('/')
    def index():
        users_lines_html = []
        users = db.get_all_users()
        for user in list(users):
            users_lines_html.append(_USER_LINE_HTML.format(user_id=user['id'], user_name=user['name']))
        users_list = '\n'.join(users_lines_html)
        index_html_page = _INDEX_HTML.format(users=users_list)
        return index_html_page

    @website.route('/users/<user_id>')
    def user(user_id):
        user_data = db.get_user_by_id(int(user_id))
        user_birthday = datetime.fromtimestamp(user_data['birthday'] / 1000).date()
        user_gender = {'m': 'Male', 'f': 'Female', 'o': 'Other'}[user_data['gender']]
        thoughts = db.get_snapshots_ts_by_user(int(user_id))
        thoughts_lines_html = []
        for thought in list(thoughts):
            thought_ts = datetime.fromtimestamp(thought['ts'] / 1000)
            thoughts_lines_html \
                .append(_THOUGHT_LINE_HTML
                        .format(user_id=user_id, timestamp=thought_ts, ts=thought['ts']))
        thought_list = '\n'.join(thoughts_lines_html)
        users_html_page = _USERS_HTML. \
            format(user_id=user_id, user_name=user_data['name'], user_gender=user_gender,
                   user_birthday=user_birthday, thoughts=thought_list)
        return users_html_page

    @website.route('/users/<user_id>/feelings_overtime')
    def feelings_overtime(user_id):
        user_data = db.get_user_by_id(int(user_id))
        feelings = db.get_feelings_by_user(int(user_id))
        feelings_lines_html = []
        for thought in list(feelings):
            if 'feelings' in thought:
                feelings_data = thought['feelings']
                feelings_lines_html.append(_FEELINGS_LINE_HTML.format(feelings_data=feelings_data))
        feelings_list = '\n'.join(feelings_lines_html)
        feelings_html_page = _FEELINGS_OVERTIME_HTML. \
            format(user_id=user_id, user_name=user_data['name'], feelings_data_overtime=feelings_list)
        return feelings_html_page

    @website.route('/users/<user_id>/pose_overtime')
    def pose_overtime(user_id):
        user_data = db.get_user_by_id(int(user_id))
        pose = db.get_poses_by_user(int(user_id))
        pose_lines_html = []
        for thought in list(pose):
            if 'rotation' in thought and 'translation' in thought:
                rotation_data = thought['rotation']
                translation_data = thought['translation']
                pose_lines_html.append(_POSE_LINE_HTML.format(rotation_data=rotation_data, translation_data=translation_data))
        pose_list = '\n'.join(pose_lines_html)
        pose_html_page = _POSE_OVERTIME_HTML. \
            format(user_id=user_id, user_name=user_data['name'], pose_data_overtime=pose_list)
        return pose_html_page

    @website.route('/users/<user_id>/color_image_overtime')
    def color_image_overtime(user_id):
        user_data = db.get_user_by_id(int(user_id))
        image_lines_html = []
        image = db.get_color_images_by_user(int(user_id))
        for thought in list(image):
            if 'color_image' in thought:
                width, height, path = thought['color_image']
                image_lines_html.append(_IMAGE_LINE_HTML.format(path=path[17:], width=width/10, height=height/10))
        image_list = '\n'.join(image_lines_html)
        image_html_page = _IMAGE_OVERTIME_HTML. \
            format(user_id=user_id, user_name=user_data['name'], image_data_overtime=image_list)
        return image_html_page

    @website.route('/users/<user_id>/depth_image_overtime')
    def depth_image_overtime(user_id):
        user_data = db.get_user_by_id(int(user_id))
        image_lines_html = []
        image = db.get_depth_images_by_user(int(user_id))
        for thought in list(image):
            if 'depth_image' in thought:
                width, height, path = thought['depth_image']
                image_lines_html.append(_IMAGE_LINE_HTML.format(path=path[17:], width=width, height=height))
        image_list = '\n'.join(image_lines_html)
        image_html_page = _IMAGE_OVERTIME_HTML. \
            format(user_id=user_id, user_name=user_data['name'], image_data_overtime=image_list)
        return image_html_page

    @website.route('/users/<user_id>/<timestamp>')
    def snapshot(user_id, timestamp):
        snapshot = db.get_snapshot_by_user_and_ts(int(user_id), int(timestamp))
        rotation = "missing"
        translation = "missing"
        feelings = "missing"
        color_image_path = ""
        color_image_height = 100
        color_image_width = 100
        depth_image_path = ""
        depth_image_height = 100
        depth_image_width = 100

        for data in snapshot:
            if data == "rotation":
                rotation = snapshot['rotation']
            if data == "translation":
                translation = snapshot['translation']
            if data == "feelings":
                feelings = snapshot['feelings']
            if data == "color_image":
                color_image_width, color_image_height, color_image_path = snapshot['color_image']
                color_image_path = color_image_path[17:]
            if data == "depth_image":
                depth_image_width, depth_image_height, depth_image_path = snapshot['depth_image']
                depth_image_path = depth_image_path[17:]
        return _SNAPSHOT_HTML.format(user_id=user_id, timestamp=timestamp, translation=translation,
                                     rotation=rotation, feelings=feelings, depth_image_width=depth_image_width,
                                     depth_image_height=depth_image_height, depth_image_path=depth_image_path,
                                     color_image_width=color_image_width, color_image_height=color_image_height,
                                     color_image_path=color_image_path)

    @website.route('/users/<user_id>/<timestamp>/<image_type>')
    def snapshot_image(user_id, timestamp, image_type):
        snapshott = db.get_snapshot_by_user_and_ts(int(user_id), int(timestamp))
        image_path = ""
        image_height = 100
        image_width = 100

        if image_type == "color-image":
            image_width, image_height, image_path = snapshott['color_image']

        if image_type == "depth-image":
            image_width, image_height, image_path = snapshott['depth_image']

        image_path = image_path[17:]
        return _IMAGE_HTML.format(image_width=image_width,
                                  image_height=image_height,
                                  image_path=image_path)


def run_server(host, port, database_url):
    if database_url.startswith("mongodb"):
        with Db(database_url) as db:
            webserver_routers(db)
            website.run(host, port)
    else:
        raise Exception("unsupported db")
