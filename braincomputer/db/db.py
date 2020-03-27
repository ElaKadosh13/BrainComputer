from pymongo import MongoClient
from pprint import pprint
import json


class Db:
    def __init__(self):
        self.client = MongoClient('mongodb://127.0.0.1:27017')
        self.mdb = self.client["mdb"]
        self.users_table = None
        self.snapshots_table = None
        #pprint(self.db.command("serverStatus"))
        print("created db!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


    def create_db(self):
        self.users_table = self.mdb["users"] # collection is same as table
        self.snapshots_table = self.mdb["snapshots"]


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


