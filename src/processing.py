def filter_by_state(original_list: list, value_state: str = "EXECUTED") -> list:
    """
        Функция принимает список словарей и опционально значение для ключа
    state, (по умолчанию 'EXECUTED') и возвращает новый список словарей state_list, содержащий только те словари,
    у которых ключ state соответствует указанному значению)
    """
    state_list = []
    for points in original_list:
        for value in points.values():
            if value == value_state:
                state_list.append(points)
    return state_list


def sort_by_date(list_date: list, sort: bool = True) -> list:
    """

    Функция принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание)
    и возвращает список new_list_date, отсортированный по дате.
    """
    sorting_date = sorted(list_date, key=lambda date: date["date"], reverse=sort)

    return sorting_date
