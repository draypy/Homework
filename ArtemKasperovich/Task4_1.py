# Implement a function which receives a string and replaces all " symbols with ' and vise versa.

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


if __name__ == "__main__":
    string = 'Any pytho\"nista l\'ike nam\"espaces a lot.'
    print(string_replace(string))
