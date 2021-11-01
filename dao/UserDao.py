from dao import ClusterSession
from model.User import User

class UserDao:
    def __init__(self):
        self.session = ClusterSession.getSession()

    def addUser(self, userId, name, email):
        add_statement = "INSERT INTO wallet.user (userid, email, name) VALUES ({0}, '{1}', '{2}');".format(userId, email, name)
        self.session.execute(add_statement)


    def getUser(self, user_id):
        get_statement = "select * from user where userid={0};".format(user_id)
        user = User(user_id)
        user_record = self.session.execute(get_statement)
        user.email = user_record[0].email
        user.name = user_record[0].name
        return user


