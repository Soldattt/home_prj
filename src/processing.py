
def filter_by_state(lists, value_state = "EXECUTED") -> list:

    """
    Функция принимает список словарей и опционально значение для ключа
state, (по умолчанию 'EXECUTED') и возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению)
    """
    state_list = []
    for dictionaries in lists:
        for value in dictionaries.values():
            if value == value_state:
                state_list.append(dictionaries)
    return state_list

