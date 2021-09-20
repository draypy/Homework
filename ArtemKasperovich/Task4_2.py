# Write a function that check whether a string is a palindrome or not.
# Usage of any reversing functions is prohibited.
# To check your implementation you can use strings from here.
from string import punctuation as punct

print(punct)


def palindrome(string_palindr):
    """This function checks whether the string is a palindrome
    """
    string_palindr = string_palindr.lower()
    if len(string_palindr) == 1:
        return f'"{string_palindr}" is palindrome'
    step_reverse = -1
    for step in range(len(string_palindr) // 2):
        if string_palindr[step] == string_palindr[step_reverse] or \
                ((string_palindr[step] and string_palindr[step_reverse]) in
                 punct or (" ", '\t', '\n', '\v', "\r")):
                 # conditions https://en.wikipedia.org/wiki/Palindrome
            step_reverse -= 1
            continue
        else:
            return f'"{string_palindr}" is not palindrome'
    return f'"{string_palindr}" is palindrome'


if __name__ == "__main__":
    print(palindrome('Лег на храм, и дивен и невидим архангел'))
    print(palindrome('h'))
    print(palindrome('Я — арка края'))
    print(palindrome('11/11/11 11:11'))
    print(palindrome("Dammit I'm Mad"))
