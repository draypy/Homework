def palindrome(string):
    """This function checks whether the string is a palindrome
    """
    if len(string) == 1:
        return f'"{string}" is palindrome'
    index_ = 0
    index_reverse = -1
    while string[index_] == string[index_reverse] and index_ >= len(string)/2:
        index_ += 1
        index_reverse -= 1
        return f'"{string}" is palindrome'
    return f'"{string}" is not palindrome'


