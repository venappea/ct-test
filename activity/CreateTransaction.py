from dao.TransactionDao import TransactionDao
from datetime import datetime
import os
from flask import jsonify
import uuid

def create_transaction_activity(address, amount, coin, type):
    try:
        dao = TransactionDao()
        transaction_id = uuid.uuid4()
        dao.createTransaction(address, amount, coin, transaction_id, type)
        return jsonify(message="Successfully added new transaction. TransactionId: {0}".format(transaction_id), hostname=os.uname()[1],
                   current_time=str(datetime.now())), 200
    except Exception as error:
        error_message = "%s: %s" % (error.__class__.__name__, str(error))
        print("DAO failed to add transaction with error: {0} ".format(error_message))
        return jsonify(message="Failed to add transaction", hostname=os.uname()[1],
                       current_time=str(datetime.now())), 500
