# Task 4.10
# Implement a function that takes a number as an argument and returns a dictionary,
# where the key is a number and the value is the square of that number.

def generate_squares(number):
    """
    A function that takes a number as an argument and returns a dictionary,
    where the key is a number, and the value is the square of this number.
    """
    return {key: key ** 2 for key in range(1, number + 1)}


if __name__ == "__main__":
    print(generate_squares(6))
