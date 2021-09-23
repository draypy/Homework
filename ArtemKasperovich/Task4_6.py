# Task 4.5
# Implement a decorator `call_once` which runs a function or method once and caches the result.
# All consecutive calls to this function should return cached result no matter the arguments.

from functools import reduce, wraps


def call_once(func):
    """
    A decorator which runs a function once and caches the result.
    All consecutive calls to this function return cached result no matter the arguments.
    """
    last_result = []

    @wraps(func)
    def wrapper(*args, **kwargs):
        last_result.append(func(*args, **kwargs))
        print(f"Last result = '{last_result[0]}'")
        return last_result[0]

    return wrapper


@call_once
def sum_of_numbers(*args):
    result = reduce(lambda x, y: x + y, args)
    print(f"Current result = '{result}'")
    return result
