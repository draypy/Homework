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
