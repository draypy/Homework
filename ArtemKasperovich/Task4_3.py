def string_split(string, separator):
    """This function implements the string method strip.
       Accepts a string and a separator as input
    """
    array_ = []
    index_ = 0
    counter = 0
    while counter < len(string):
        if string[counter] == separator:
            array_.append(string[index_:counter])
            index_ = counter + 1
        counter += 1
    return array_


s = 'bla bla bla bla bla bla'
b = "b"
print(string_split(s, b))

