import os

from src.reading_data import open_csv_file, open_excel_file

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
test_path_empty_csv = os.path.join(project_root, "tests", "test_data", "test_transactions.csv")
test_path_excel = os.path.join(project_root, "tests", "test_data", "test_transactions.xlsx")


def test_notfound_file_csv():
    result = open_csv_file("../data/transactions1.csv")
    assert result == "Файл не найден"


def test_empty_file_csv():
    result = open_csv_file(test_path_empty_csv)
    assert result == "Ошибка в данных файла"


def test_notfound_file():
    result = open_excel_file("../data/transactions_excel1.xlsx")
    assert result == "Файл не найден"


def test_empty_file():
    result = open_excel_file(test_path_excel)
    assert result == "Ошибка в данных файла"
