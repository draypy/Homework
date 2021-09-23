# Task 4.5
# Implement a decorator remember_result which remembers last result of function
# it decorates and prints it before next call.
from functools import reduce, wraps


def remember_result(func):
    """
    This decorator remembers last result of function it decorates and prints it before next call.
    """
    last_result = [None]

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Last result = '{last_result[-1]}'")
        last_result.append(func(*args, **kwargs))
        return last_result[-1]

    return wrapper


@remember_result
def sum_list(*args):
    result = reduce(lambda x, y: x + y, args)
    print(f"Current result = '{result}'")
    return result
