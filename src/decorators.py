from functools import wraps


def log(filename):
    """ Декоратор, который логирует начало и конец выполнения функции, а также ее результаты и ошибки"""
    def log_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result
            except TypeError:
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: TypeError. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: TypeError. Inputs: {args}, {kwargs}")
                raise TypeError
        return wrapper
    return log_decorator
