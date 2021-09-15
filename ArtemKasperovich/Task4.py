### Task 1.4
# Write a Python program to sort a dictionary by key.

dct = {
    '1.0': 'Gendalf',
    '3': 'Morgoth',
    '2.5': "Legolas",
    '4': 'Sam',
    '20.111111111111111': 'Frodo'
}

for key in sorted(dct.keys(), key=float):
    print(f"{key}: {dct[key]}")
