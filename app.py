# pylint: disable=broad-except,invalid-name
"""
    Sample Flask app testing Cassandra connection
"""
import os
from datetime import datetime
from flask import Flask, jsonify, request

from cassandra.cluster import Cluster

from activity.AddUserWallet import add_user_wallet_activity
from activity.GetUserWallet import get_user_wallet_activity
from activity.AddUser import add_user_activity
from activity.GetUser import get_user_activity
from activity.CreateTransaction import create_transaction_activity
from activity.GetTransaction import get_transaction_activity
from activity.DetectTransferActivity import get_user_transaction_history_activity
app = Flask(__name__)

@app.route('/v1/wallet/', methods=['POST', 'GET'])
def wallet():
    if request.method == 'POST':
        data = request.get_json()
        response = add_user_wallet_activity(data['userId'], data['address'])
        return response
    else:
        data = request.get_json()
        response = get_user_wallet_activity(data['userId'])
        return response

@app.route('/v1/user/', methods=['POST', 'GET'])
def user():
    if request.method == 'POST':
        data = request.get_json()
        response = add_user_activity(data['name'], data['email'])
        return response
    else:
        data = request.get_json()
        response = get_user_activity(data['user_id'])
        return response

@app.route('/v1/transaction/', methods=['POST', 'GET'])
def transaction():
    if request.method == 'POST':
        data = request.get_json()
        response = create_transaction_activity(data['address'], data['amount'], data['coin'], data['type'])
        return response
    else:
        data = request.get_json()
        response = get_transaction_activity(data['address'])
        return response

@app.route('/v1/user/transaction', methods=['GET'])
def user_transactions():
    data = request.get_json()
    response = get_user_transaction_history_activity(data['userId'])
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

