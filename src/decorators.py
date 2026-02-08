from typing import Any

# from time import time

"""
Декоратор принимает на вход параметр filename(название файла) и записывает в него результат выполнения функцию
Если параметр не задан, то результаты выводятся в консоль
"""


def log(filename: Any = None) -> Any:
    def wrapper(func: Any) -> Any:
        def inner(*args: Any, **kwargs: Any) -> Any:

            try:
                result = func(*args, **kwargs)
                message = f"my_function ok\n" f"Результат: {result}\n"

            except Exception as e:
                message = f"my_function error: {type(e)} {args}\n"

            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(message)
            else:
                print(message)

        return inner

    return wrapper
