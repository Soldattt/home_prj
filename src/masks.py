import logging
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
masks_log = os.path.join(project_root, "logs", "masks.log")


masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(masks_log, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход тип и номер карты в виде строки и возвращает маску номера по правилу: name_card
    XXXX XX** **** XXXX"""
    masks_logger.info("Принимаем на вход номер карты")
    if card_number == "":
        masks_logger.warning("Некорректный номер карты")
        card_mask = "Введите корректный номер"
    elif card_number.isdigit() is False:
        masks_logger.warning("Некорректный номер карты")
        card_mask = "Введите корректный номер"
    elif len(card_number) < 15:
        masks_logger.warning("Некорректный номер карты")
        card_mask = "Введите корректный номер"
    else:
        masks_logger.info("Формируем и выводим маску номера карты")
        card_mask = f"{card_number[-16:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"

    return card_mask


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета в виде строки и возвращает маску номера по правилу: Счет
    **XXXX"""
    masks_logger.info("Принимаем на вход номер счета")
    if len(account_number) < 6:
        masks_logger.warning("Некорректный номер счета")
        account_mask = "Введите корректный номер"
    elif account_number.isdigit() is False:
        masks_logger.warning("Некорректный номер счета")
        account_mask = "Введите корректный номер"
    else:
        masks_logger.info("Формируем и выводим маску номера счета")
        account_mask = f"Счет **{account_number[-4:]}"

    return account_mask
