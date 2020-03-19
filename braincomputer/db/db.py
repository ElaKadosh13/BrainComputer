from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import json


class Db:
    def __init__(self):
        self.session = None
        self.engine = None

    def create_db(self):
        self.engine = create_engine('sqlite:///tmp/db.sqlite3')
        metadata = MetaData()
        self.pose_table = PoseTable(metadata)
        self.feelings_table = FeelingsTable(metadata)
        self.image_table = ImageTable(metadata)
        self.users_table = UsersTable(metadata)
        metadata.create_all(self.engine)
        #delete all tables - metadata.drop_all(engine)

    def save_to_db(self, data, parser):
        json_data = json.loads(data)
        print("in save to db")
        insert = None
        user = json_data['user']
        user_id = user['id']
        user_query = self.users_table.query(user_id)
        connection = self.engine.connect()
        result = connection.execute(user_query)
        if not result.first():
             print("new user")
             insert_user = self.users_table.insert(user_id, user['name'], user['birthday'], user['gender'])
             connection.execute(insert_user)

        #todo if user doesnt exist add it to users table
        #user_name  user_birthday, user_feelings = user
        print("!!!!!!!!!")
        if parser == 'pose':
            print("'''in pose")
            rotation_x, rotation_y, rotation_z, rotation_w = json_data['rotation']
            translation_x, translation_y, translation_z = json_data['translation']
            insert = self.pose_table.insert(user_id, rotation_x, rotation_y, rotation_z, rotation_w, translation_x, translation_y, translation_z)
        if parser == 'feelings':
            feelings_x, feelings_y, feelings_z, feelings_w = json_data['feelings']
            insert = self.feelings_table.insert(user_id, feelings_x, feelings_y, feelings_z, feelings_w)
        if parser == 'color_image' or parser == 'depth_image':
            width = json_data['width']
            height = json_data['height']
            path = json_data['path']
            insert = self.image_table.insert(user_id, width, height, path, parser)


        result = connection.execute(insert)

        #todo - delte those prints
        print(result.inserted_primary_key)
        if parser == 'pose':
            query = select([self.pose_table.table])
        if parser == 'feelings':
            query = select([self.feelings_table.table])
        if parser == 'color_image' or parser == 'depth_image':
            query = select([self.image_table.table])
        for row in connection.execute(query):
            print(dict(row))
        print("users table!!!!")
        q = select([self.users_table.table])
        for row in connection.execute(q):
            print(dict(row))


class PoseTable:
    def __init__(self, metadata):
        self.table = Table('pose_db', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('userid', Integer, nullable=False),
                    Column('rotation_x', Integer, nullable=False),
                    Column('rotation_y', Integer, nullable=False),
                    Column('rotation_z', Integer, nullable=False),
                    Column('rotation_w', Integer, nullable=False),
                    Column('translation_x', Integer, nullable=False),
                    Column('translation_y', Integer, nullable=False),
                    Column('translation_z', Integer, nullable=False))

    def insert(self, userid, rotation_x, rotation_y, rotation_z, rotation_w, translation_x, translation_y, translation_z):
        print("try insert pose")
        return self.table.insert().values(userid=userid,
                                    rotation_x=rotation_x,
                                   rotation_y=rotation_y,
                                   rotation_z=rotation_z,
                                   rotation_w=rotation_w,
                                   translation_x=translation_x,
                                   translation_y=translation_y,
                                   translation_z=translation_z)


class FeelingsTable:
    def __init__(self, metadata):
        self.table = Table('feelings_db', metadata,
                           Column('id', Integer, primary_key=True),
                           Column('userid', Integer, nullable=False),
                           Column('feelings_x', Integer, nullable=False),
                           Column('feelings_y', Integer, nullable=False),
                           Column('feelings_z', Integer, nullable=False),
                           Column('feelings_w', Integer, nullable=False))

    def insert(self, userid, feelings_x, feelings_y, feelings_z, feelings_w):
        return self.table.insert().values(userid=userid,
                                   feelings_x=feelings_x,
                                   feelings_y=feelings_y,
                                   feelings_z=feelings_z,
                                   feelings_w=feelings_w)


class ImageTable:
    def __init__(self, metadata):
        self.table = Table('images_db', metadata,
                           Column('id', Integer, primary_key=True),
                           Column('userid', Integer, nullable=False),
                           Column('width', Integer, nullable=False),
                           Column('height', Integer, nullable=False),
                           Column('path', String, nullable=False),
                           Column('type', String, nullable=False))

    def insert(self, userid, width, height, path, type):
        return self.table.insert().values(userid=userid,
                                   width=width,
                                   height=height,
                                   path=path,
                                   type=type)


class UsersTable:
    def __init__(self, metadata):
        self.table = Table('users_db', metadata,
                           Column('id', Integer, primary_key=True),
                           Column('userid', Integer, nullable=False),
                           Column('name', String, nullable=False),
                           Column('birthday', Integer, nullable=False),
                           Column('gender', String, nullable=False))

    def insert(self, userid, name, birthday, gender):
        print("in insert")
        return self.table.insert().values(userid=userid,
                                          name=name,
                                          birthday=birthday,
                                          gender=gender)

    def query(self, user_id):
        print("in qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")
        print(user_id)
        return select([self.table]).where(self.table.columns.userid == user_id)
