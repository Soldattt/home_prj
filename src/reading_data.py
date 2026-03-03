import os
from typing import Any

import pandas as pd
from pandas.errors import EmptyDataError

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_csv = os.path.join(project_root, "data", "transactions.csv")
path_excel = os.path.join(project_root, "data", "transactions_excel.xlsx")


def open_csv_file(path: str) -> Any:
    """
    Функция считывает финансовые операции из файла .csv по указываемому и выдает список словарей с транзакциями
    """
    try:
        try:
            csv_reader = pd.read_csv(path, encoding="utf-8")
            return csv_reader
        except EmptyDataError:
            return "Ошибка в данных файла"
    except FileNotFoundError:
        return "Файл не найден"


def open_excel_file(path: str) -> Any:
    """
    Функция считывает финансовые операции из файла .xlsx по указываемому пути и выдает список словарей с транзакциями
    """
    try:
        try:
            excel_reader = pd.read_excel(path)
            not_null_excel_reader = excel_reader.loc[excel_reader.id.notnull()]
            return not_null_excel_reader
        except ValueError:
            return "Ошибка в данных файла"
    except FileNotFoundError:
        return "Файл не найден"
