# Write a function that check whether a string is a palindrome or not.
# Usage of any reversing functions is prohibited.
# To check your implementation you can use strings from here.

def palindrome(string):
    """This function checks whether the string is a palindrome
    """
    string = string.lower()
    if len(string) == 1:
        return f'"{string}" is palindrome'
    step_reverse = -1
    for step in range(len(string) // 2):
        if string[step] == string[step_reverse]:
            step_reverse -= 1
            continue
        else:
            return f'"{string}" is not palindrome'
    return f'"{string}" is palindrome'


if __name__ == "__main__":
    print(palindrome('lol'))
    print(palindrome('h'))
    print(palindrome('ha'))
