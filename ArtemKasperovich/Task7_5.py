# Task 7.5
# Implement function for check that number is even, at least 3.
# Throw different exceptions for this errors.
# Custom exceptions must be derived from custom base exception(not Base Exception class).

class CustomException(Exception):
    pass


def even(number):
    if number % 2 == 0:
        if number < 3:
            raise CustomException('Number less then 3')
        if not isinstance(number, (int, float)):
            raise TypeError('Number must be an int type')
        return True
    return False


print(even(3))
