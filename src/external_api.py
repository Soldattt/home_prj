import os


import requests
from dotenv import load_dotenv




load_dotenv()

API_KEY = os.getenv("API_KEY")


def operation_amount(transaction: list[dict] | dict) -> list[float]:
    """
    Функция возвращает сумму операции в рублях
    """

    result = []
    for transact in transaction:

        if transact != {}:
            currency = transact.get('operationAmount').get('currency').get('code')
            amount_cur = float(transact.get('operationAmount').get('amount'))
            if currency != 'RUB':
                response = requests.get(f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/RUB/{amount_cur}')
                if response.status_code == 200:
                    data = response.json()
                    amount = round(float(data.get('conversion_result')),2)
                    result.append(amount)
            else:
                 result.append(amount_cur)
    return result












