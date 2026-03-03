import json
import logging
import os
from typing import Any

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
utils_log = os.path.join(project_root, "logs", "utils.log")


utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(utils_log, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)


def valute_transaction(path: str = "../data/operations.json") -> Any:
    try:
        utils_logger.info("Проверяем наличие файла по указанному пути")
        try:
            utils_logger.info("Производим перевод данных файла в объект Python")
            with open(f"{path}", "r", encoding="utf-8") as f:
                result = json.load(f)
                utils_logger.info("Окончание выполнения работы с файлом")
                return result
        except json.JSONDecodeError as ex:
            utils_logger.error(f"{ex} - Ошибка данных файла")
            return "Ошибка в данных файла"
    except FileNotFoundError as ex:
        utils_logger.error(f"{ex} - Ошибка пути файла")
        return "Указанный файл не найден"
