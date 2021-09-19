# Task 4.8
# Implement a function get_pairs(lst: List) -> List[Tuple] which returns a list of tuples containing pairs of elements.
# Pairs should be formed as in the example.
# If there is only one element in the list return None instead. Example:
def get_pairs(array):
    """
     The function returns a list of pairs of tuples of values
    """
    return [(array[iter_ - 1], array[iter_]) for iter_ in range(1, len(array))] or None


if __name__ == "__main__":
    print(get_pairs([1, 2, 3, 8, 9]))
    print(get_pairs(['need', 'to', 'sleep', 'more']))
    print(get_pairs([1]))