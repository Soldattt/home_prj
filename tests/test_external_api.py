from unittest.mock import patch

import requests

from src.external_api import operation_amount


def test_api_rus(api_rus):
    result = operation_amount(
        [
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
    )

    assert result == api_rus


def test_api_none(api_none):
    result = operation_amount([{}])
    assert result == api_none


def api_usd(val):
    response = requests.get(f"https://v6.exchangerate-api.com/v6/123/pair/{val}/RUB/1.0")
    return response.json()


@patch("requests.get")
def test_api_usd(mock_get):
    mock_get.return_value.json.return_value = [76.58]
    assert api_usd("USD") == [76.58]
    mock_get.assert_called_once_with("https://v6.exchangerate-api.com/v6/123/pair/USD/RUB/1.0")
