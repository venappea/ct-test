from dao.UserDao import UserDao
from datetime import datetime
import os
from flask import jsonify

def get_user_activity(user_id):
    try:
        dao = UserDao()
        user = dao.getUser(user_id)
        return jsonify(message=user.__str__(), hostname=os.uname()[1],
                   current_time=str(datetime.now())), 200
    except Exception as error:
        error_message = "%s: %s" % (error.__class__.__name__, str(error))
        print("DAO failed to get user with error: {0} ".format(error_message))
        return jsonify(message="Failed to add user", hostname=os.uname()[1],
                       current_time=str(datetime.now())), 500
