from dao.AddressesDao import AddressesDao
from dao.TransactionDao import TransactionDao


class TransactionAddressInfo:
    def __init__(self, timestamp, address, transaction_id):
        self.timestamp = timestamp
        self.address = address
        self.transaction_id = transaction_id


def detect_transfers_for_user(user_id):
    address_dao = AddressesDao()
    transaction_dao = TransactionDao()
    address_records = address_dao.getUserWalletAddresses(user_id)
    wallets = address_records.addresses
    transaction_dict = _build_transaction_information(transaction_dao, wallets)
    valid_transactions_ids = []
    output = []
    for wallet_address in wallets:
        wallet_transactions = transaction_dao.getTransaction(wallet_address)
        for transaction_index in range(len(wallet_transactions)):
            transaction = wallet_transactions[transaction_index]
            search_key = None
            if transaction.type == 'in':
                search_key = "{0}-{1}-{2}".format(transaction.amount, 'out', transaction.coin)
            else:
                search_key = "{0}-{1}-{2}".format(transaction.amount, 'in', transaction.coin)

            if search_key in transaction_dict.keys():
                # validation logic here

                for address_info_index in range(len(transaction_dict[search_key])):
                    address_information = transaction_dict[search_key][address_info_index]
                    print(address_information.address, transaction.address)
                    if transaction.address != address_information.address and \
                            address_information.address not in valid_transactions_ids:
                        if transaction.type == 'out':
                            ## widthdraws can only happen before deposits so verify timestamps make sense
                            if transaction.timestamp < address_information.timestamp:

                                ## Success, we add it to the list. set the address as visited to true
                                ## We also break from this loop because we already found a matching pair so it can move now to
                                ## next element
                                output.append((transaction.transaction_id, address_information.transaction_id))
                                wallet_transactions.pop(transaction_index)
                                transaction_dict[search_key].pop(address_info_index)
                                break

                        else:
                            # its an deposit so its the opposite
                            if transaction.timestamp > address_information.timestamp:
                                ## Success!
                                output.append((address_information.transaction_id, transaction.transaction_id))
                                wallet_transactions.pop(transaction_index)
                                transaction_dict[search_key].pop(address_info_index)
                                break

    return output


def _build_transaction_information(transaction_dao, wallet_records):
    transaction_dict = dict()
    for wallet_address in wallet_records:
        wallet_transactions = transaction_dao.getTransaction(wallet_address)
        for transaction in wallet_transactions:
            amount_type_coin_key = "{0}-{1}-{2}".format(transaction.amount, transaction.type, transaction.coin)
            if amount_type_coin_key not in transaction_dict.keys():
                transaction_dict[amount_type_coin_key] = []
            transaction_dict[amount_type_coin_key].append(
                TransactionAddressInfo(transaction.timestamp, transaction.address, transaction.transaction_id))

    return transaction_dict
