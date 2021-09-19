# Task 4.9
# Implement a bunch of functions which receive a changeable number of strings and return next parameters:
# characters that appear in all strings
# characters that appear in at least one string
# characters that appear at least in two strings
# characters of alphabet, that were not used in any string
# Note: use string.ascii_lowercase for list of alphabet letters
from string import ascii_lowercase as alphabet


def search(strings):
    """
    Iterates through the strings creates a dictionary {"letter": "count in strings"}
    """
    counter = {}
    for string in strings:
        for letter in string:
            counter[letter] = counter.get(letter, 0) + 1
    return counter


def test_1(strings):
    """
    Returns the letters that are in each line
    """
    characters = search(strings)
    return [key for key, value in characters.items() if value == len(strings)]


def test_2(strings):
    """
    Returns the letters that are at least in one line
    """
    characters = search(strings)
    return [key for key, value in characters.items() if value > 1]


def test_3(strings):
    """
    Returns the letters that are at least in two lines
    """
    characters = search(strings)
    return [key for key, value in characters.items() if value > 2]


def test_4(strings):
    """
    Returns the letters,that were not used in any string
    """
    characters = search(strings)
    return [letter for letter in alphabet if letter not in characters.keys()]


if __name__ == "__main__":
    test_strings = ["hello", "world", "python", ]
    print(test_1(test_strings))
    print(test_2(test_strings))
    print(test_3(test_strings))
    print(test_4(test_strings))
