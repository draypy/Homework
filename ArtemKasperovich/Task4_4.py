def split_by_index(string, indexes):
    """This function splits the specified string string by the indexes of the indexes list.
        If the index does not match the string, it is ignored
    """
    result = []
    index_ = 0
    for digit in indexes:
        if digit > len(string):
            continue
        result.append(string[index_: digit])
        index_ = digit
    result.append(string[indexes[-1]:])
    return result

