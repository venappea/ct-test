from dao.AddressesDao import AddressesDao
from datetime import datetime
import os
from flask import jsonify

def add_user_wallet_activity(userId, address):
    try:
        dao = AddressesDao()
        dao.addUserWalletAddress(userId, address)
        return jsonify(message="Successfully added new wallet", hostname=os.uname()[1],
                   current_time=str(datetime.now())), 200
    except Exception as error:
        error_message = "%s: %s" % (error.__class__.__name__, str(error))
        print("DAO failed to add transaction with errorr: {0} ".format(error_message))
        return jsonify(message="Failed to add new transaction", hostname=os.uname()[1],
                       current_time=str(datetime.now())), 500
