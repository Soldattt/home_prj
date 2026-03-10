from typing import Generator


def filter_by_currency(transactions: list, currency: str = "USD") -> Generator:
    """
     Функция принимает список описания банковских операций и опциональное значение (валюту)
    currency, (по умолчанию "USD") и возвращает новый список, содержащий только те операции,
    в которых указана заданная валюта.
    """
    transact = (
        x
        for x in transactions
        for k, v in x.items()
        if k == "operationAmount"
        for key, value in v.items()
        if key == "currency"
        for s, d in value.items()
        if s == "code" and d == currency
    )

    return transact


def transaction_descriptions(transactions: list) -> Generator:
    """
    Функция принимает список описания банковских операций и возвращает описание каждой операции по очереди.
    """
    for x in transactions:
        for k in x.keys():
            if k == "description":
                description = x.get("description")
                yield description


def card_number_generator(start: int = 0, stop: int = 0) -> Generator:
    """
    Функция генерирует номер карты в виде ХХХХ ХХХХ ХХХХ ХХХХ основываясь на заданных значениях начала и конца
    генерации от 0000 0000 0000 0000 до 9999 9999 9999 9999
    """
    for x in range(start, stop + 1):
        card = f"{x:0>16}"
        yield card[:4] + " " + card[4:8] + " " + card[8:12] + " " + card[12:16]
