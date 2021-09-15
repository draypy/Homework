### Task 1.5
# Write a Python program to print all unique values of all dictionaries in a list.
# Examples:
# ```
# Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
import json
data = json.loads(input())
print(list(set([value for dct in data for value in dct.values()])))
