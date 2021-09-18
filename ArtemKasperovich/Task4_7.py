def foo(List):
    """
    This function returns a list of integers in such a way that each element is the product
    of all the elements of the old one with the exception of one
    """
    import operator
    from functools import reduce
    multiplication_digit = reduce(operator.mul, List)
    return [multiplication_digit // digit for digit in List]


print(foo([1, 2, 3, 4, 5]))
