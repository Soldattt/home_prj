from typing import Any

# from time import time


def log(filename: Any = None) -> Any:
    def wrapper(func: Any) -> Any:
        def inner(*args: Any, **kwargs: Any) -> Any:
            """
            Декоратор принимает на вход параметр filename(название файла)
            и записывает в него результат выполнения функцию
            Если параметр не задан, то результаты выводятся в консоль
            """

            result = None
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok\n" f"Результат: {result}\n"

            except Exception as e:
                message = f"{func.__name__} error: {type(e)} {args}\n"

            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(message)
            else:
                print(message)
            return result

        return inner

    return wrapper
