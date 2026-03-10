import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция принимает список транзакций и параметр search, по которому необходимо произвести
    сортировку и возвращает отсортированный список
    """

    pattern = re.compile(search, re.IGNORECASE)  # Игнорируем регистр для поиска

    result = []

    for record in data:
        state = record.get("state")
        if pattern.search(str(state)):
            result.append(record)
    return result


def counter_operations(data:list[dict]) -> dict:
    """
    Функция принимает список транзакций и посчитывает операции по категориям в описании каждой операции,
    а далее возвращает словарь с количеством каждых операций
    """
    categories = []

    for operation in data:
        description = operation["description"]
        categories.append(description)
    count = Counter(categories)

    return dict(count)
