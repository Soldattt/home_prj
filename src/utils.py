import json
from typing import Any


def valute_transaction(path: str = "../data/operations.json") -> Any:
    try:
        try:
            with open(f"{path}", "r", encoding="utf-8") as f:
                result = json.load(f)
                return result
        except json.JSONDecodeError:
            return "Ошибка в данных файла"
    except FileNotFoundError:
        return "Указанный файл не найден"
