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

    def save_to_db(self, data, parser):
        json_data = json.loads(data)
        print("in save to db")
        insert = None
        if parser == 'pose':
            print("'''in pose")
            rotation_x, rotation_y, rotation_z, rotation_w = json_data['rotation']
            translation_x, translation_y, translation_z = json_data['translation']
            insert = self.pose_table.insert(42, rotation_x, rotation_y, rotation_z, rotation_w, translation_x, translation_y, translation_z)
        if parser == 'feelings':
            feelings_x, feelings_y, feelings_z, feelings_w = json_data
            insert = self.feelings_table.insert(42, feelings_x, feelings_y, feelings_z, feelings_w)
        if parser == 'color_image' or parser == 'depth_image':
            width = json_data['width']
            height = json_data['height']
            path = json_data['path']
            insert = self.image_table.insert(42, width, height, path, parser)

        connection = self.engine.connect()
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
        return self.table.insert().values(userid=userid,
                                          name=name,
                                          birthday=birthday,
                                          gender=gender)
