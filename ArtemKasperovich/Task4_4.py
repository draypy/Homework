# Implement a function split_by_index(s: str, indexes: List[int]) -> List[str] which splits the s string by indexes specified in indexes.
# Wrong indexes must be ignored. Examples:

def split_by_index(string, indexes):
    """This function splits the specified string string by the indexes of the indexes list.
        If the index does not match the string, it is ignored
    """
    result = []
    index_ = 0
    for digit in indexes:
        try:
            if string[digit] in string:
                result.append(string[index_:digit])
            index_ = digit
        except IndexError:
            result.append(string)
    return result


if __name__ == "__main__":
    print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
    print(split_by_index("no luck", [42]))
