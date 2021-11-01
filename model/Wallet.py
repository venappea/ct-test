class Wallet:
    def __init__(self, userId):
        self.userId = userId
        self.addresses = []

    def __str__(self):
        return f'UserId:{self.userId} and addresses: {self.addresses}'
