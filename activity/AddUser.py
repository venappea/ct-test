from dao.UserDao import UserDao
from datetime import datetime
import os
from flask import jsonify
import uuid

def add_user_activity(name, email):
    try:
        dao = UserDao()
        userId = uuid.uuid4()
        dao.addUser(userId, name, email)
        return jsonify(message="Successfully added new user. userId: {0}".format(userId), hostname=os.uname()[1],
                   current_time=str(datetime.now())), 200
    except Exception as error:
        error_message = "%s: %s" % (error.__class__.__name__, str(error))
        print("DAO failed to add user with error: {0} ".format(error_message))
        return jsonify(message="Failed to add user", hostname=os.uname()[1],
                       current_time=str(datetime.now())), 500
