from braincomputer.db.mongodb import Mongodb


class Db:
    """If you want to change the db just change lines 21-22 to the new db initialization.
    Make sure the db implements the methods: save_to_db, all the get_ queries
    Also - all functions use *args so it's easy to replace to a db that needs different arguments for those methods
    """
    def __init__(self, db_url):
        self.db = None
        split_addr = db_url.replace("/", "").split(":")
        if len(split_addr) != 3:
            raise Exception("invalid url, need to be db://host:port")
        if split_addr[0] == 'mongodb':
            self.db = Mongodb(db_url)
        else:
            raise Exception("currently only mongodb is supported")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.close_db()

    def save_to_db(self, *args):
        self.db.save_to_db(*args)

    def close_db(self):
        self.db.close_db()

    def get_all_users(self):
        return self.db.get_all_users()

    def get_user_by_id(self, *args):
        return self.db.get_user_by_id(*args)

    def get_snapshots_ts_by_user(self, *args):
        return self.db.get_snapshots_ts_by_user(*args)

    def get_snapshot_by_user_and_ts(self, *args):
        return self.db.get_snapshot_by_user_and_ts(*args)

    def get_feelings_by_user(self, *args):
        return self.db.get_feelings_by_user(*args)

    def get_poses_by_user(self, *args):
        return self.db.get_poses_by_user(*args)

    def get_color_images_by_user(self, *args):
        return self.db.get_color_images_by_user(*args)

    def get_depth_images_by_user(self, *args):
        return self.db.get_depth_images_by_user(*args)
