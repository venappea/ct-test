from dao.TransactionDao import TransactionDao
from datetime import datetime
import os
from flask import jsonify
import json
def get_transaction_activity(address):
    try:
        dao = TransactionDao()
        transactions = dao.getTransaction(address)
        json_string = json.dumps([ob.__str__() for ob in transactions])

        return jsonify(message=json_string, hostname=os.uname()[1],
                   current_time=str(datetime.now())), 200
    except Exception as error:
        error_message = "%s: %s" % (error.__class__.__name__, str(error))
        print("DAO failed to get transaction with error: {0} ".format(error_message))
        return jsonify(message="Failed to add transaction", hostname=os.uname()[1],
                       current_time=str(datetime.now())), 500
