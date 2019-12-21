

class User:
    def __init__(self, user_id, user_name, user_birthday, user_gender):
        self.user_id = user_id
        self.user_name = user_name
        self.user_birthday = user_birthday
        self.user_gender = user_gender

    def __repr__(self):
        return f'User(user_id={self.user_id}, user_name={self.user_name}, user_birthday={self.user_birthday}, ' \
               f'user_gender={self.user_gender})'
