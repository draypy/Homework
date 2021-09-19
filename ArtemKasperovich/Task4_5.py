# Task 4.5
# Implement a function get_digits(num: int) ->
# -> Tuple[int] which returns a tuple of a given integer's digits. Example:
def get_digit(num: int):
    """
    This function converts the number num to a tuple of integers
    """
    return tuple((map(int, str(num))))


if __name__ == "__main__":
    print(get_digit(87178291199))
