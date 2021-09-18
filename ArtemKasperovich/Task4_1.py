def string_replace(string):
    """
    The function that changes ' to " The argument is a string
    """
    result = ""
    for symbol in string:
        if symbol == '\"':
            result += "\'"
            continue
        elif symbol == "\'":
            result += '\"'
            continue
        result += symbol
    return result

