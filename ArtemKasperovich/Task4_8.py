def get_pairs(array):
    """
     The function returns a list of pairs of tuples of values
    """
    if len(array) == 1:
        return None
    return [(array[iter_-1], array[iter_]) for iter_ in range(1, len(array))]

lst = [1, 2, 3, 8, 9,10]

print(get_pairs((lst)))