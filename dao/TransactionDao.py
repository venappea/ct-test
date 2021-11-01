from dao import ClusterSession
from model.Transaction import Transaction
from datetime import datetime

class TransactionDao:
    def __init__(self):
        self.session = ClusterSession.getSession()

    def createTransaction(self, address, amount, coin, transaction_id, type):
        add_statement = "INSERT INTO wallet.transaction " \
                        "(address, timestamp, amount, coin, transactionid, type) " \
                        "VALUES ('{0}', {1}, {2}, '{3}', {4}, '{5}');".format(address, datetime.now().timestamp(),
                                                                                       amount, coin, transaction_id, type)
        print(add_statement)
        self.session.execute(add_statement)


    def getTransaction(self, address):
        get_statement = "select * from transaction where address='{0}';".format(address)
        print(get_statement)
        transaction_records = self.session.execute(get_statement)
        transactions =[]
        for record in transaction_records:
            transactions.append(Transaction(record.timestamp, record.transactionid, record.address, record.amount, record.type, record.coin))
        return transactions