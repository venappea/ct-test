from dao import ClusterSession
from model.Wallet import Wallet

class AddressesDao:
    def __init__(self):
        self.session = ClusterSession.getSession()

    def addUserWalletAddress(self, userId, address):
        add_statement = "INSERT INTO wallet.addresses (userid, address) VALUES ({0}, '{1}');".format(userId, address)
        self.session.execute(add_statement)

    def getUserWalletAddresses(self, user_id):
        user_wallet = Wallet(user_id)
        get_statement = "select * from addresses where userid={0};".format(user_id)
        user_addresses_records = self.session.execute(get_statement)
        for record in user_addresses_records:
            user_wallet.addresses.append(record[1])
        return user_wallet

