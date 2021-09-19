# Implement a function which works the same as str.split method
# (without using str.split itself, of course).

def string_split(string, separator=' ', max_split=-1):
    """This function implements the string method strip.
       Accepts a string and a separator as input
    """
    if separator in string:
        result, index = [], 0
        while len(result) != max_split:
            fnd = string.find(separator, index)
            if fnd == -1:
                result.append(string[index:])
                break
            result.append(string[index:fnd])
            index = fnd + len(separator)
        if len(result) == max_split:
            result.append(string[index:])
    else:
        return f"['{string}']"
    return result


if __name__ == "__main__":
    s = 'bla, bla, bla, bla, bla, bla, bla '
    sep = "s"
    print(string_split(s, sep, 4))
    print(s.split('s', maxsplit=4))
    sep = ", "
    print(string_split(s, sep))
    print(s.split(', '))
    sep = ' '
    print(string_split(s, sep, max_split=2))
    print(s.split(' ', maxsplit=2))
