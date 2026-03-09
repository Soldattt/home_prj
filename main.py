import re

from src.reading_data import open_csv_file, open_excel_file
from src.transactions_for_user import counter_operations, process_bank_search
from src.utils import valute_transaction
from src.widget import get_date, mask_account_card


def main() -> str | dict:
    """
    Основная функция для запуска программы, считывает информацию из выбранного файла и передает
    в модуль transactions_for_user, производит сбор информации от пользователя через запросы, сортирует транзакции
    на основании выбора пользователя и выводит результат выполнения работы программы
    """
    data = None
    user_search = None
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    valid_user_selection = False
    valid_user_search = False
    while not valid_user_selection:
        user_selection = input(
            "Укажите номер пункта, откуда хотите получить данные:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла \n"
        )
        if user_selection in ["1", "2", "3"]:
            valid_user_selection = True
            while not valid_user_search:
                user_search = str(
                    input(
                        "\nВведите статус, по которому необходимо выполнить фильтрацию.\n"
                        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
                    )
                ).upper()
                if user_search in ["EXECUTED", "CANCELED", "PENDING"]:
                    valid_user_search = True

                    if user_selection == "1":
                        print("\nДля обработки данных выбран JSON-файл")
                        print(f"Для фильтрации выбран статус {user_search}\n")
                        data = valute_transaction()

                    elif user_selection == "2":
                        print("\nДля обработки данных выбран CSV-файл")
                        print(f"Для фильтрации выбран статус {user_search}\n")
                        data = open_csv_file()

                    elif user_selection == "3":
                        print("\nДля обработки данных выбран XLSX-файл")
                        print(f"Для фильтрации выбран статус {user_search}\n")
                        data = open_excel_file()

                else:
                    print(
                        f"\nСтатус {user_search} недоступен."
                        f" Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
                    )

        else:
            print("\nУкажите корректный пункт")
    sorting_date = None
    print("\nОтсортировать операции по дате?")
    valid_user_sorting = False
    while not valid_user_sorting:
        user_sorting = str(input("Введите да\нет:\n")).lower()
        if user_sorting in ["да", "нет"]:
            valid_user_sorting = True
            if user_sorting == "да":
                print("\nОтсортировать по возрастанию или по убыванию?")
                valid_user_direction = False
                while not valid_user_direction:
                    user_direction = str(input("Введите по возрастанию\по убыванию:\n")).lower()
                    if user_direction in ["по возрастанию", "по убыванию"]:
                        valid_user_direction = True
                        if user_direction == "по возрастанию":
                            sorting_date = sorted(
                                process_bank_search(data, user_search), key=lambda date: date["date"], reverse=False
                            )
                        else:
                            sorting_date = sorted(
                                process_bank_search(data, user_search), key=lambda date: date["date"], reverse=True
                            )

                    else:
                        print("\nВведите только по возрастанию или по убыванию")
            else:
                sorting_date = process_bank_search(data, user_search)
        else:
            print("\nВведите только да или нет")
    new_list = []
    print("\nВыводить только рублевые транзакции?")
    valid_user_currency = False
    while not valid_user_currency:
        user_currency = str(input("Введите да\нет:\n")).lower()
        if user_currency in ["да", "нет"]:
            valid_user_currency = True
            if user_currency == "да":
                for operation in sorting_date:
                    for v in operation.values():
                        if v == "RUB":
                            new_list.append(operation)
            else:
                new_list = sorting_date
        else:
            print("\nВведите только да или нет")
    result_list = []
    print("\nОтфильтровать список транзакций по определенному слову в описании?")
    valid_user_operation = False
    while not valid_user_operation:
        user_operation = str(input("Введите да\нет:\n")).lower()
        if user_operation in ["да", "нет"]:
            valid_user_operation = True
            if user_operation == "да":
                user_category = input("\nВведите слово: \n")
                if user_category:
                    pattern_category = re.compile(user_category, re.IGNORECASE)
                    for record in new_list:
                        description = record.get("description")
                        if pattern_category.search(str(description)):
                            result_list.append(record)
            else:
                result_list = new_list
        else:
            print("\nВведите только да или нет")

    if result_list:
        print()
        print(counter_operations(result_list))
        print()
        for operation in result_list:
            date = operation.get("date")
            description = operation.get("description")
            operation_from = str(operation.get("from"))
            operation_to = str(operation.get("to"))
            amount = operation.get("amount")
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

    return "\nБлагодарим, что пользовались нашей продукцией"


if __name__ == "__main__":
    print(main())
