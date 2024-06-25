import functools
import logging


def log(filename=None):
    """Декоратор для логирования вызова функции и её результата.
         Если указан filename, логирование будет происходить в файл, иначе в консоль."""
    if filename:
        logging.basicConfig(
            filename=filename, level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    logging.info(
                        f"Function {func.__name__} called with args: {args} kwargs: {kwargs}. Result: {result}"
                    )
                else:
                    print(f"Function {func.__name__} called with args: {args} kwargs: {kwargs}. Result: {result}")
                return result
            except Exception as e:
                if filename:
                    logging.error(f"Function {func.__name__} error: {str(e)}, args: {args} kwargs: {kwargs}")
                else:
                    print(f"Function {func.__name__} error: {str(e)}, args: {args} kwargs: {kwargs}")

        return wrapper

    return decorator


@log("logs.txt")  # Логи будут записываться в файл logs.txt
def add(a, b):
    return a + b


result = add(2, 3)


@log()  # Логи будут выводиться в консоль
def divide(a, b):
    return a / b


result = divide(6, 2)
