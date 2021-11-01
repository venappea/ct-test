class User:
    def __init__(self, user_id):
        self.name = None
        self.email = None
        self.user_id = user_id


    def __str__(self):
        return f'UserId:{self.user_id}  & name: {self.name} & email: {self.email}'