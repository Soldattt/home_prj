from src.utils import valute_transaction


def test_notfound_file():
    result = valute_transaction("../data/operations1.json")
    assert result == "Указанный файл не найден"


def test_empty_file():
    result = valute_transaction("test_data/test_operation.json")
    assert result == "Ошибка в данных файла"


def test_open_file():
    result = valute_transaction("../tests/test_data/test_operation_1.json")
    assert result == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]
