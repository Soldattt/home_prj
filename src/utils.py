import json
from typing import Any


def valute_transaction(path: str = "../data/operations.json") -> Any:

    try:
        with open(f"{path}", "r", encoding="utf-8") as f:
            transaction = json.load(f)
            return transaction
    except Exception:
        raise FileNotFoundError
