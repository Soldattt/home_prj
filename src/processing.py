def filter_by_state(lists: list, value_state: str = "EXECUTED") -> list:
    """
        Функция принимает список словарей и опционально значение для ключа
    state, (по умолчанию 'EXECUTED') и возвращает новый список словарей state_list, содержащий только те словари,
    у которых ключ state соответствует указанному значению)
    """
    state_list = []
    for dictionaries in lists:
        for value in dictionaries.values():
            if value == value_state:
                state_list.append(dictionaries)
    return state_list


def sort_by_date(list_date: list, sort: bool = False) -> list:
    """

    Функция принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание)
    и возвращает список new_list_date, отсортированный по дате.
    """
    new_list_date = sorted(list_date, key=lambda date: date["date"], reverse=sort)

    return new_list_date
