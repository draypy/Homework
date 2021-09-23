# Task 4.2
# Implement a function which search for most common words in the file.
# Use `data/lorem_ipsum.txt` file as a example.

import re


def most_common_words(filepath, number_of_words=3):
    """
    Search for most common words in the file
    """
    with open(filepath) as file:
        words = {}
        for line in file:
            for word in re.findall(r"\w+", line.lower()):
                words[word] = words.get(word, 0) + 1
        sorted_words = sorted(words.items(), key=lambda arg: arg[1], reverse=True)
    return [word[0] for word in sorted_words[:number_of_words]]

