import enum


class TransactionType(enum.Enum):
    IN = 'IN'
    OUT = 'OUT'


class Transaction:
    def __init__(self, timestamp, transaction_id, address, amount, type, coin):
        self.timestamp = timestamp
        self.transaction_id = transaction_id
        self.address = address
        self.amount = amount
        self.type = type
        self.coin = coin

    def __str__(self):
        return f'timestamp:{self.timestamp} ' \
               f'transaction_id: {self.transaction_id} ' \
               f'& address: {self.address} ' \
               f'amount: {self.amount} ' \
               f'& type: {self.type} ' \
               f'& coin: {self.coin}'