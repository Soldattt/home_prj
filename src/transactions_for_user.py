import re
from collections import Counter

from src.widget import get_date, mask_account_card


def process_bank_search(
    data: list[dict], search: str, user_sorting, user_direction, user_currency, user_category
) -> str | dict:
    """
    Функция принимает список транзакций и параметры, по которым необходимо производить сортировку на основании выборов
    пользователя и возвращает отсортированный список
    """

    pattern = re.compile(search, re.IGNORECASE)  # Игнорируем регистр для поиска

    result = []

    for record in data:
        state = record.get("state")
        if pattern.search(str(state)):
            result.append(record)

    if user_sorting == "да":
        if user_direction == "по возрастанию":
            sorting_date = sorted(result, key=lambda date: date["date"], reverse=False)

        else:
            sorting_date = sorted(result, key=lambda date: date["date"], reverse=True)
    else:
        sorting_date = result

    new_list = []

    if user_currency == "да":
        for operation in sorting_date:
            for v in operation.values():
                if v == "RUB":
                    new_list.append(operation)
    else:
        new_list = sorting_date

    result_list = []
    if user_category:
        pattern_category = re.compile(user_category, re.IGNORECASE)
        for record in new_list:
            description = record.get("description")
            if pattern_category.search(str(description)):
                result_list.append(record)
        return counter_operations(result_list)
    else:
        return counter_operations(new_list)


def counter_operations(data):
    """
    Функция принимает список транзакций и посчитывает операции по категориям в описании каждой операции,
    а далее возвращает список транзакций и словарь с количеством каждых операций
    """
    categories = ["Перевод с карты на карту", "Перевод со счета на счет", "Открытие вклада", "Перевод организации"]

    count = Counter()
    for operation in data:
        description = operation["description"]
        for x in categories:
            if description == x:
                count[x] += 1
    return transaction_output(data, dict(count))


def transaction_output(data: list[dict], sum_operations: dict) -> str | dict:
    """
    Функция принимает список транзакций и словарь счетчика, формирует и выводит сообщение с результатом работы
    программы пользователю или сообщение <Не найдено ни одной транзакции, подходящей под ваши условия фильтрации>
    """

    if data:
        print()
        print(sum_operations)
        print()
        for operation in data:
            date = operation.get("date")
            description = operation.get("description")
            operation_from = str(operation.get("from"))
            operation_to = str(operation.get("to"))
            amount = int(operation.get("amount"))
            currency_code = operation.get("currency_code")
            if operation_from == "nan":
                result = (
                    f"{get_date(date)} {description}\n"
                    f"{mask_account_card(operation_to)}\n"
                    f"Сумма: {amount} {currency_code}\n\n"
                )
                print(result)

            else:
                result = (
                    f"{get_date(date)} {description}\n"
                    f"{mask_account_card(operation_from)} -> {mask_account_card(operation_to)}\n"
                    f"Сумма: {amount} {currency_code}\n\n"
                )
                print(result)
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    return "\nCпасибо, что пользовались нашей продукцией"
