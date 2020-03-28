import os
import pathlib
from datetime import datetime

from flask import Flask

from braincomputer.db import Db

_INDEX_HTML = '''
<html>
    <head>
        <title>Brain Computer Interface</title>
    </head>
    <body>
        <ul>
            {users}
        </ul>
    </body>
</html>
'''
_USER_LINE_HTML = '''
<li><a href="/users/{user_id}">User: {user_id}</a></li>
'''
_USERS_HTML = '''
<html>
    <head>
        <title>Brain Computer Interface: User {user_id}</title>
    </head>
    <body>
        <p>Name: {user_name}</p>
         <p>Gender: {user_gender}</p> 
         <p>Birthday: {user_birthday}</p>
         <p>Snapshots timestamps: </p>
        <ul>
            {thoughts}
        </ul>
    </body>
</html>
'''
_THOUGHT_LINE_HTML = '''
<li><a href="/users/{user_id}/{ts}">Timestamp: {timestamp}</a></li>
'''

_SNAPSHOT_HTML = '''
<html>
    <head>
        <title>brain computer interface: user {user_id} timestamp: {timestamp}</title>
    </head>
    <body>
        <p>user {user_id} timestamp: {timestamp}</p>
        <p>pose:</br>translation: {translation}</br>rotation: {rotation}</p>
        <p>feelings:{feelings}</p>
        <p>color_image: </br> <img alt="color image missing" src={color_image_path} width={color_image_width}, height={color_image_height}></p>
        <p>depth_image: </br> <img alt="depth image missing" src={depth_image_path} width={depth_image_width}, height={depth_image_height}></p>
   </body>
</html>
'''

root_path = pathlib.Path(__file__).absolute().parent.parent
directory_path = ""
website = Flask(__name__)


def webserver_routers(db):
    @website.route('/')
    def index():
        print("in index")
        users_lines_html = []
        print(db.client.list_database_names())
        users = db.get_all_users()
        print(users)
        for user in list(users):
            print(user)
            id = user['id']
            users_lines_html.append(_USER_LINE_HTML.format(user_id=id))
        users_list = '\n'.join(users_lines_html)
        index_html_page = _INDEX_HTML.format(users=users_list)
        # create the index html
        return index_html_page

    ##todo - replace thought by snapshot
    @website.route('/users/<user_id>')
    def user(user_id):
        print("user_page!!!!!!")
        print(user_id)
        user_data = db.get_user_by_id(int(user_id))
        user_birthday = datetime.fromtimestamp(user_data['birthday'] / 1000).date()
        user_gender = {'m': 'Male', 'f': 'Female', 'o': 'Other'}[user_data['gender']]
        print(user_data)
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

    @website.route('/users/<user_id>/<timestamp>')
    def snapshot(user_id, timestamp):
        print("snapshot page")
        snapshot = db.get_snapshot_by_user_and_ts(int(user_id), int(timestamp))
        print(snapshot)
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


def run_server(host, port, db_url):
    if db_url.startswith("mongodb"):
        db = Db(db_url)
        webserver_routers(db)
        website.run(host, port)
        # todo - db.client.close()
    else:
        raise Exception("unsupported db")
