

def filter_by_state(original_list: list, value_state: str = "EXECUTED") -> list:
    """
        Функция принимает список словарей и опционально значение для ключа
    state, (по умолчанию 'EXECUTED') и возвращает новый список словарей state_list, содержащий только те словари,
    у которых ключ state соответствует указанному значению)
    """
    state_list = []
    if value_state != "CANCELED":
        value_state = "EXECUTED"

    for points in original_list:
        for value in points.values():
            if value == value_state:
                state_list.append(points)
    return state_list


def sort_by_date(list_date: list, sort: bool = True) -> list:
    """
    Функция принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание)
    и возвращает список sorting_date, отсортированный по дате.
    """
    sorting_date: list = []
    for x in list_date:
        for key, value in x.items():
            if key == "date" and len(value) != 26:
                sorting_date = ["Некорректный список"]
            else:
                sorting_date = sorted(list_date, key=lambda date: date["date"], reverse=sort)

    return sorting_date
