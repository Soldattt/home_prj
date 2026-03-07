import json
import os
from typing import Any

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_json = os.path.join(project_root, "data", "operations.json")
path = path_json


def valute_transaction(path: str) -> Any:
    try:

        try:

            with open(f"{path}", "r", encoding="utf-8") as f:
                result = json.load(f)

                return result
        except json.JSONDecodeError as ex:

            return "Ошибка в данных файла"
    except FileNotFoundError as ex:

        return "Указанный файл не найден"
