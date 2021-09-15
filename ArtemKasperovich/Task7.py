# Task 1.6
# Write a program which makes a pretty print of a part of the multiplication table.
# Examples:
# ```
# Input:
# a = 2
# b = 4
# c = 3
# d = 7

# Output:
# 	3	4	5	6	7
# 2	6	8	10	12	14
# 3	9	12	15	18	21
# 4	12	16	20	24	28

first_clm_number = int(input('Enter a first_clm_number: '))
second_clm_number = int(input('Enter a second_clm_number'))
if first_clm_number > second_clm_number:
    first_clm_number, second_clm_number = second_clm_number, first_clm_number
first_boundary_value = int(input('Enter a first_boundary_value'))
second_boundary_value = int(input('Enter a second_boundary_value'))
if first_boundary_value > second_boundary_value:
    first_boundary_value, second_boundary_value = second_boundary_value, first_boundary_value

upper_row = list(range(first_boundary_value, second_boundary_value + 1))
print('\t', end='')
print(*upper_row, sep='\t')
for elem in range(first_clm_number, second_clm_number + 1):
    print(elem, end='\t')
    for item in upper_row:
        print(item * elem, end='\t')
    print()
