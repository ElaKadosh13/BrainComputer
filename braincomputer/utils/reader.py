import gzip
import struct
import os
from braincomputer import messages_pb2
from braincomputer.protocol import Snapshot
from braincomputer.utils.image import ColorImage, DepthImage
from datetime import datetime

from braincomputer.utils.user import User


class Reader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_size = os.path.getsize(self.file_path)
        self.user, self.offset = Reader.get_user_data(file_path)
        self.snapshots = self.iterate_snapshots()

    def __repr__(self):
        return f'user: {self.user.user_id}: {self.user.user_name}, born ' \
               f'{datetime.fromtimestamp(self.user.user_birthday).strftime("%d-%m-%Y")} ({self.user.user_gender})'

    def __iter__(self):
        return iter(self.snapshots)

    @classmethod
    def get_user_data(cls, file_path):
        with gzip.open(file_path, 'rb') as file_stream:
            size, = struct.unpack('I', file_stream.read(4))
            user = messages_pb2.User()
            user.ParseFromString(file_stream.read(size))
            user_id = user.user_id
            user_name = user.username
            user_birthday = user.birthday
            genders = {0: "male", 1: "female", 2: "other"}
            user_gender = genders[user.gender]
            return User(user_id, user_name, user_birthday, user_gender), (size + 4)

    def iterate_snapshots(self):
        with gzip.open(self.file_path, 'rb') as file_stream:
            file_stream.seek(self.offset)
            while self.file_size - self.offset > 0:
                snapshot, offset = self.get_snapshot_data(file_stream)
                self.offset += offset
                yield snapshot

    def get_snapshot_data(self, file_stream):
        size, = struct.unpack('I', file_stream.read(4))
        snapshot = messages_pb2.Snapshot()
        snapshot.ParseFromString(file_stream.read(size))
        dattime = snapshot.datetime
        translation = (snapshot.pose.translation.x, snapshot.pose.translation.y, snapshot.pose.translation.z)
        rotation = (snapshot.pose.rotation.x, snapshot.pose.rotation.y, snapshot.pose.rotation.z, snapshot.pose.rotation.w)
        color_image = ColorImage(snapshot.color_image.width, snapshot.color_image.height, snapshot.color_image.data)
        depth_image = DepthImage(snapshot.depth_image.width, snapshot.depth_image.height, snapshot.depth_image.data)
        user_feelings = (snapshot.feelings.hunger, snapshot.feelings.thirst,
                         snapshot.feelings.exhaustion, snapshot.feelings.happiness)
        return Snapshot(dattime, translation, rotation, color_image, depth_image, user_feelings), (size + 4)


def start_reader(file_path):
    reader = Reader(file_path)
    print(reader)
    print()
    # todo - delete
    x = 0
    for snapshot in reader:
        print(snapshot)
        print()
