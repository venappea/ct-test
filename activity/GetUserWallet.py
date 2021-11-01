from dao.AddressesDao import AddressesDao
from datetime import datetime
import os
from flask import jsonify

def get_user_wallet_activity(userId):
    print("Request received to get wallet addresses for userId: {0}".format(userId))
    wallet = get_user_wallet(userId)
    print(wallet.__str__())
    return jsonify(message=wallet.__str__(), hostname=os.uname()[1],
                   current_time=str(datetime.now())), 200
    return response

def get_user_wallet(userId):
    try:
        dao = AddressesDao()
        return dao.getUserWalletAddresses(userId)
    except Exception as error:
        error_message = "%s: %s" % (error.__class__.__name__, str(error))
        print("failed to get user wallet addresses with error {0}".format(error_message))
        return jsonify(message="Failed to get user wallet", hostname=os.uname()[1],
                       current_time=str(datetime.now())), 500

