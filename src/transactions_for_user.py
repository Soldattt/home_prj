import re
from collections import Counter

from src.widget import get_date, mask_account_card


def process_bank_search(data: list[dict], search: str, user_sorting, user_direction, user_currency) -> str:
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

    sorting_date = None
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

    return process_bank_operations(new_list)


def process_bank_operations(data: list[dict]) -> str:
    """
    Функция принимает список транзакций и запрашивает информацию для сортировки по описанию операции, а также считает
    количество транзакций по наименованию операций и передает новый или существующий список транзакций и
    словарь счетчика
    """
    data_list = data
    result = []
    count: dict = Counter()
    print("\nОтфильтровать список транзакций по определенной операции в описании?")
    valid_user_operation = False
    while not valid_user_operation:
        user_operation = str(input("Введите да\нет:\n")).lower()
        if user_operation in ["да", "нет"]:
            valid_user_valute = True
            if user_operation == "да":
                valid_user_category = False
                while not valid_user_category:
                    category = input(
                        "\nУкажите пункт категории: \n"
                        "1.Перевод организации \n"
                        "2.Открытие вклада\n"
                        "3.Перевод со счета на счет\n"
                        "4.Перевод с карты на карту\n"
                    )
                    if category in ["1", "2", "3", "4"]:
                        valid_user_category = True
                        if category == "1":
                            for operation in data_list:
                                for v in operation.values():
                                    if v == "Перевод организации":
                                        count[v] += 1
                                        result.append(operation)
                        if category == "2":
                            for operation in data_list:
                                for v in operation.values():
                                    if v == "Открытие вклада":
                                        count[v] += 1
                                        result.append(operation)
                        if category == "3":
                            for operation in data_list:
                                for v in operation.values():
                                    if v == "Перевод со счета на счет":
                                        count[v] += 1
                                        result.append(operation)
                        if category == "4":
                            for operation in data_list:
                                for v in operation.values():
                                    if v == "Перевод с карты на карту":
                                        count[v] += 1
                                        result.append(operation)
                        return transaction_output(result, dict(count))

                    else:
                        print("\nУкажите корректный пункт")

            else:
                categories = [
                    "Перевод с карты на карту",
                    "Перевод со счета на счет",
                    "Открытие вклада",
                    "Перевод организации",
                ]
                count = Counter()
                for operation in data_list:
                    description = operation["description"].lower()
                    for category in categories:
                        if re.search(re.escape(category.lower()), description):
                            count[category] += 1

        else:
            print("\nВведите только да или нет")


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
