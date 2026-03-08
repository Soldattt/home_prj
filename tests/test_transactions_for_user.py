import os


from src.transactions_for_user import process_bank_search

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_json = os.path.join(project_root, "data", "operations.json")


def test_incorrect_process_search():
    data = [
        {
            "id": 650703.0,
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    user_search = "EXECUTED"
    result = process_bank_search(data, user_search)
    assert result == "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"


def test_process_search():
    data = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    user_search = "CANCELED"
    result = process_bank_search(data, user_search)
    assert result == "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
