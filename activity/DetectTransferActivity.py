from datetime import datetime
import os
from flask import jsonify
from components.TransferDetector import detect_transfers_for_user

def get_user_transaction_history_activity(user_id):
    transactions = detect_transfers_for_user(user_id)
    return jsonify(message="Transactions for user_id {0} is {1}".format(user_id, transactions), hostname=os.uname()[1],
                current_time=str(datetime.now())), 200
