# Task 4.6
# Implement a function get_shortest_word(s: str) -> str which returns the longest word in the given string.
# The word can contain any symbols except whitespaces ( , \n, \t and so on).
# If there are multiple longest words in the string with a same length return the word that occures first. Example:
def get_shortest_word(string):
    """
     This function finds the longest word without special characters(\n,\t etc)
    """
    variable_string = ""
    result = []
    for symbol in string:
        if symbol.isalpha():
            variable_string += symbol
        else:
            result.append(variable_string)
            variable_string = ""
    return max(*result, key=len)


if __name__ == "__main__":
    print(get_shortest_word('Python is simple and effective!'))
    print(get_shortest_word('Any pythonista like namespaces a lot.'))
