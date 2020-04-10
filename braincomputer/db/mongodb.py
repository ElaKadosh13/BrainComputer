from pymongo import MongoClient
import json


class Mongodb:
    def __init__(self, db_url):
        self.client = MongoClient(db_url)
        self.mdb = self.client["mdb"]
        self.users_table = self.mdb["users"]
        self.snapshots_table = self.mdb["snapshots"]

    def save_to_db(self, data):
        json_data = json.loads(data)
        user = json_data['user']
        self.users_table.update_one({'id': user['id']}, {'$set': {**user}}, upsert=True)
        json_data['ts'] = json_data['ts'][0]
        json_data['user'] = user['id']
        snapshot_id = str(user['id']) + "_" + str(json_data['ts'])
        self.snapshots_table.update_one({'id': snapshot_id}, {'$set': {**json_data}}, upsert=True)

    def close_db(self):
        self.client.close()

    def get_all_users(self):
        return self.users_table.find({}, {"_id": 0, "id": 1, "name": 1})

    def get_user_by_id(self, user_id):
        return self.users_table.find_one({'id': user_id})

    def get_snapshots_ts_by_user(self, user_id):
        return self.snapshots_table.find({"user": user_id}, {"_id": 0, "ts": 1})

    def get_snapshot_by_user_and_ts(self, user_id, timestamp):
        return self.snapshots_table.find_one({"user": user_id, "ts": timestamp})

    def get_feelings_by_user(self, user_id):
        return self.snapshots_table.find({"user": user_id}, {"_id": 0, "feelings": 1})

    def get_poses_by_user(self, user_id):
        return self.snapshots_table.find({"user": user_id}, {"_id": 0, "rotation": 1, "translation": 1})

    def get_color_images_by_user(self, user_id):
        return self.snapshots_table.find({"user": user_id}, {"_id": 0, "color_image": 1})

    def get_depth_images_by_user(self, user_id):
        return self.snapshots_table.find({"user": user_id}, {"_id": 0, "depth_image": 1})


