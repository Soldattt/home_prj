import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def operation_amount(transaction: dict) -> Any[float]:
    """
    Функция принимает список транзакций и возвращает список с суммой каждой транзакции в рублях
    """
    if transaction != {}:  # если список на входе не пустой, вычисляем валюту и сумму транзакции
        currency = transaction.get("operationAmount").get("currency").get("code")
        amount_cur = float(transaction.get("operationAmount").get("amount"))

        if currency != "RUB":  # если транзакция не в рублях, следующий запрос производит конвертирование суммы
            response = requests.get(f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/RUB/{amount_cur}")
            data = response.json()

            return round(float(data.get("conversion_result")), 2)

        else:
            return amount_cur
    else:
        pass
