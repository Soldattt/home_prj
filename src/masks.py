def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход тип и номер карты в виде строки и возвращает маску номера по правилу: name_card
    XXXX XX** **** XXXX"""
    if card_number == "":
        card_mask = "Введите корректный номер"
    elif card_number.isdigit() is False:
        card_mask = "Введите корректный номер"
    elif len(card_number) < 15:
        card_mask = "Введите корректный номер"
    else:
        card_mask = f"{card_number[-16:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"

    return card_mask


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета в виде строки и возвращает маску номера по правилу: Счет
    **XXXX"""
    if len(account_number) < 6:
        account_mask = "Введите корректный номер"
    elif account_number.isdigit() is False:
        account_mask = "Введите корректный номер"
    else:
        account_mask = f"Счет **{account_number[-4:]}"

    return account_mask
