import os

from src.decorators import log


def test_log_in_console(capsys):
    @log()
    def add_numbers(a, b):
        return a + b

    add_numbers(2, 3)

    capture = capsys.readouterr()
    assert "add_numbers ok\nРезультат: 5" in capture.out


@log(filename="test_log.txt")
def my_function_sum(x, y):
    return x + y


def test_my_function_file_output():
    my_function_sum(2, 3)
    with open("test_log.txt", "r", encoding="utf-8") as file:
        content = file.read()
    assert "my_function_sum ok\nРезультат: 5" in content
    os.remove("test_log.txt")


def test_log_error(capsys):
    @log()
    def add_numbers(a, b):
        return a + b

    add_numbers("", 3)

    capture = capsys.readouterr()
    assert "add_numbers error: <class 'TypeError'> ('', 3)\n" in capture.out
