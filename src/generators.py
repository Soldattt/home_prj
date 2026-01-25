def filter_by_currency(transaction_list: list, currency: str = "USD") -> list:
    new_transaction_list = []
    for x in transaction_list:
        for k, v  in x.items():
            if k == "operationAmount":
                transaction = {}
                transaction.update(v)
                for key, value in transaction.items():
                    if key == "currency":
                        transact = {}
                        transact.update(v)
                        for val in transact.values():
                            if val == currency:
                                new_transaction_list.append(x)
                                break

    return new_transaction_list


