# Task 1.3
# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
# Input: ['red', 'white', 'black', 'red', 'green', 'black']
# Output: ['black', 'green', 'red', 'white', 'red']

result = {word for word in input('Please enter a string\n').split(', ')}  # red, black, red, white, green
print(sorted(result))
