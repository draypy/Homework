# Task 7.4
# Implement decorator for supressing exceptions.
# If exception not occure write log to console.
from contextlib import suppress
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with suppress(AttributeError):
            func(*args, **kwargs)

    return wrapper


@my_decorator
def function(a=0):
    print(function.__name__)
    a.read()


function()


@my_decorator
def function_error(a=0):
    print(function_error.__name__)
    print(0 / a)


function_error()
