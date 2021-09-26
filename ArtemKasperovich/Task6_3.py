# Task 6.3
# Implement The Keyword encoding and decoding for latin alphabet.
# The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
# Add the provided keyword at the begining of the alphabet.
# A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet.
# Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching
# to A, B, C etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used
# in alphabetical order, excluding those already used in the key.
# Encryption:
# Keyword is "Crypto"
# * A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# * C R Y P T O A B D E F G H I J K L M N Q S U V W X Z



class Cipher:
    def __init__(self, keyword):
        from string import ascii_uppercase as alphabet
        self.alphabet = alphabet + ' '
        self.keyword = keyword

    @staticmethod
    def crypto_alpha(crypto_string, alphabet):
        crypto_string = crypto_string.upper()
        for letter in alphabet:
            if letter not in crypto_string:
                crypto_string += letter
        return crypto_string

    def encode(self, string_in):
        self.keyword = self.crypto_alpha(self.keyword, self.alphabet)
        string_out = ''
        for letter in string_in:
            if letter.islower():
                index_ = self.alphabet.find(letter.upper())
                string_out += self.keyword[index_].lower()
                continue
            index_ = self.alphabet.find(letter)
            string_out += self.keyword[index_]

        return string_out

    def decode(self, string_in):
        self.keyword = self.crypto_alpha(self.keyword, self.alphabet) + " "
        string_out = ''
        for letter in string_in:
            if letter.islower():
                letter = letter.upper()
                index_ = self.keyword.find(letter)
                string_out += self.alphabet[index_].lower()
                continue
            index_ = self.keyword.find(letter)
            string_out += self.alphabet[index_]
        return string_out


cipher = Cipher('table')
print(cipher.encode('Hello world'))
print(cipher.decode("Fejjn wnqjl"))
