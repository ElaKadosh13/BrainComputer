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
        # self.users_table = Table('users', metadata,
        #             Column('id', Integer, primary_key=True),
        #             Column('username', String, nullable=False),
        #             Column('gender', String, nullable=False),
        #             Column('birthday', String, nullable=False))
        self.translation_table = Table('translations', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('x', Integer, nullable=False),
                    Column('y', Integer, nullable=False),
                    Column('z', Integer, nullable=False))
        metadata.create_all(self.engine)

    def save_to_db(self, parser_name, data):
        print("in save to db")
        json_data = json.loads(data)
        x, y, z = json_data
        #todo change user id
        insert = self.translation_table.insert().values(x=x, y=y, z=z)
        connection = self.engine.connect()
        result = connection.execute(insert)
        print(result.inserted_primary_key)
        query = select([self.translation_table])
        for row in connection.execute(query):
            print(dict(row))