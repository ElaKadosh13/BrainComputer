from pymongo import MongoClient
from pprint import pprint
import json


class Db:
    def __init__(self, db_url):
        self.client = MongoClient(db_url)#'mongodb://127.0.0.1:27017')
        self.mdb = self.client["mdb"]
        self.users_table = self.mdb["users"]
        self.snapshots_table = self.mdb["snapshots"]
        #pprint(self.db.command("serverStatus"))
        print("created db!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    def save_to_db(self, data):
        json_data = json.loads(data)
        print("in save to db")
        user = json_data['user']
        self.users_table.update_one({'id': user['id']}, {'$set': {**user}}, upsert=True)
        for x in self.users_table.find():
            print(x)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        json_data['ts'] = json_data['ts'][0]
        json_data['user'] = user['id']
        snapshot_id = str(user['id']) + "_" + str(json_data['ts'])
        print(type(json_data['ts']))
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        self.snapshots_table.update_one({'id': snapshot_id}, {'$set': {**json_data}}, upsert=True)
        #todo - dont store user data and ts in snapshots table
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        for x in self.snapshots_table.find():
            print(x)

    def get_all_users(self):
        # all_users_ids = self.users_table.find({}, {"_id": 0, "id": 1, "name": 1})
        # print("get all users")
        # print(list(all_users_ids))
        # return list(all_users_ids)
        return self.users_table.find({}, {"_id": 0, "id": 1, "name": 1})

    def get_user_by_id(self, user_id):
        return self.users_table.find_one({'id': user_id})

    def get_snapshots_ts_by_user(self, user_id):
        return self.snapshots_table.find({"user": user_id}, {"_id": 0, "ts": 1})

    def get_snapshot_by_user_and_ts(self, user_id, timestamp):
        print(timestamp)
        return self.snapshots_table.find_one({"user": user_id, "ts": timestamp})

        # @classmethod
        # def connect_to_db(cls, db_url):
        #     return Db(db_url)



