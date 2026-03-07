from src.reading_data import open_csv_file, open_excel_file
from src.transactions_for_user import process_bank_search
from src.utils import valute_transaction


def main() -> str:
    """
    Основная функция для запуска программы, производит сбор информации от пользователя через запросы, считывает
    информацию из выбранного файла и передает ее в модуль transactions_for_user
    """
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
                        result = process_bank_search(data, user_search)
                        return result

                    elif user_selection == "2":
                        print("\nДля обработки данных выбран CSV-файл")
                        print(f"Для фильтрации выбран статус {user_search}\n")
                        data = open_csv_file()
                        result = process_bank_search(data, user_search)
                        return result

                    elif user_selection == "3":
                        print("\nДля обработки данных выбран XLSX-файл")
                        print(f"Для фильтрации выбран статус {user_search}\n")
                        data = open_excel_file()
                        result = process_bank_search(data, user_search)
                        return result
                else:
                    print(
                        f"\nСтатус {user_search} недоступен."
                        f" Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
                    )

        else:
            print("\nУкажите корректный пункт")


if __name__ == "__main__":
    print(main())
