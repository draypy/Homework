# Task 4.1
# Open file `data/unsorted_names.txt` in data folder.
# Sort the names and write them to a new file called `sorted_names.txt`.
# Each name should start with a new line as in the following example:


with open("../data/unsorted_names.txt") as file_unsorted:
    with open("./sorted.names.txt", 'w') as file_sorted:
        names = sorted([line for line in file_unsorted.readlines()])
        for name in names:
            file_sorted.write(name)
