def mask_account_card(card_account: str) -> str:
    """Принимает на вход тип и номер карты или номер счета в виде строк и возвращает маски карты или счета по правилу:
    name_card XXXX XX** **** XXXX или Счет **XXXX"""
    if len(card_account) == 25:
        mask = f"Счет **{card_account[-4:]}"
    elif "0" not in card_account:
        mask = "Введите корректные данные"
    elif "a" not in card_account:
        mask = "Введите корректные данные"
    elif len(card_account) < 20:
        mask = "Введите корректные данные"
    else:
        mask = f"{card_account[:-16]}{card_account[-16:-12]} {card_account[-12:-10]}** **** {card_account[-4:]}"

    return mask


def get_date(date_name: str) -> str:
    """Принимает на вход дату и время и возвращает строку в виде: ДД.ММ.ГГГГ"""

    if len(date_name) != 26:
        date_mask = "Введите корректную дату"
    else:
        date_mask = f"{date_name[8:10]}.{date_name[5:7]}.{date_name[:4]}"

    return date_mask
