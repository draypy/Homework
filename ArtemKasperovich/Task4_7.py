# Task 4.7
# Implement a function foo(List[int]) -> List[int] which, given a list of integers,
# return a new list such that each element at index i of the new list is the product of all the numbers
# in the original array except the one at i. Example:
import operator
from functools import reduce


def foo(array):
    """
    This function returns a list of integers in such a way that each element is the product
    of all the elements of the old one with the exception of one
    """

    multiplication_digit = reduce(operator.mul, array)
    return [multiplication_digit // digit for digit in array]


if __name__ == "__main__":
    print(foo([1, 2, 3, 4, 5]))
    print(foo([3, 2, 1]))
