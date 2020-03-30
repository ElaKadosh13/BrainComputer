import os
import pathlib
from datetime import datetime

from PIL.Image import Image
from flask import Flask

from braincomputer.db import Db
from flask import jsonify

root_path = pathlib.Path(__file__).absolute().parent.parent
directory_path = ""
website = Flask(__name__, static_folder="../static/")


def webserver_routers(db):
    @website.route('/users')
    def users():
        users = list(db.get_all_users())
        return jsonify(users)

    @website.route('/users/<user_id>')
    def user(user_id):
        user_data = db.get_user_by_id(int(user_id))
        if not user_data:
            return jsonify(missing_error)
        user_data.pop('_id')
        user_data['birthday'] = datetime.fromtimestamp(user_data['birthday'] / 1000)
        user_data['gender'] = {'m': 'Male', 'f': 'Female', 'o': 'Other'}[user_data['gender']]
        return jsonify(user_data)

    @website.route('/users/<user_id>/snapshots')
    def snapshots(user_id):
        snapshots_list = list(db.get_snapshots_ts_by_user(int(user_id)))
        if not snapshots_list:
            return jsonify(missing_error)
        for snapshot in snapshots_list:
            snapshot['id'] = f"{user_id}_{snapshot['ts']}"
            snapshot['ts'] = datetime.fromtimestamp(snapshot['ts'] / 1000)
        return jsonify(snapshots_list)

    @website.route('/users/<user_id>/snapshots/<snapshot_id>')
    def snapshot(user_id, snapshot_id):
        try:
            snapshot_ts = snapshot_id.split("_")[1]
        except:
            return jsonify("Error: snapshot id must have format: userid_timestamp")
        snapshot_data = db.get_snapshot_by_user_and_ts(int(user_id), int(snapshot_ts))
        if not snapshot_data:
            return jsonify(missing_error)
        snapshot_data.pop('_id')
        snapshot_data['ts'] = datetime.fromtimestamp(snapshot_data['ts'] / 1000)
        return jsonify(snapshot_data)

    @website.route('/users/<user_id>/snapshots/<snapshot_id>/<result_name>')
    def result(user_id, snapshot_id, result_name):
        snapshot_ts = snapshot_id.split("_")[1]
        snapshot_data = db.get_snapshot_by_user_and_ts(int(user_id), int(snapshot_ts))
        if not snapshot_data:
            return jsonify(missing_error)
        if result_name == "pose":
            return jsonify({'rotation': snapshot_data['rotation'], 'translation': snapshot_data['translation']})
        if result_name == "feelings":
            return jsonify(snapshot_data["feelings"])
        if result_name == "color-image":
            return jsonify(snapshot_data["color_image"])
        if result_name == "depth-image":
            return jsonify(snapshot_data["depth_image"])
        else:
            return jsonify(result_error)

    @website.route('/users/<user_id>/snapshots/<snapshot_id>/<result_name>/data')
    def result_data(user_id, snapshot_id, result_name):
        snapshot_ts = snapshot_id.split("_")[1]
        snapshot_data = db.get_snapshot_by_user_and_ts(int(user_id), int(snapshot_ts))
        if not snapshot_data:
            return jsonify(missing_error)
        if result_name == "color-image":
            return jsonify(snapshot_data["color_image"][2])
        if result_name == "depth-image":
            return jsonify(snapshot_data["depth_image"][2])
        else:
            return jsonify(result_error)


missing_error = "Error: data is missing. Make sure your arguments are valid."
result_error = "Error: Result type not supported."


def run_server(host, port, db_url):
    if db_url.startswith("mongodb"):
        db = Db(db_url)
        webserver_routers(db)
        website.run(host, port)
        # todo - db.client.close()
    else:
        raise Exception("unsupported db")
