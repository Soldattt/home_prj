import json



def valute_transaction():
    try:
        with open('../data/operations.json', 'r', encoding='utf-8') as f:
            transaction = json.load(f)
        return transaction
    except (json.JSONDecodeError, IOError):
        return []










