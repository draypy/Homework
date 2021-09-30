# Implement your custom collection called MyNumberCollection.
# It should be able to contain only numbers. It should NOT inherit any other collections.
# If user tries to add a string or any non numerical object there, exception `TypeError` should be raised.
# Method init sholud be able to take either
# `start,end,step` arguments, where `start` - first number of collection,
# `end` - last number of collection or some ordered iterable
# collection (see the example).
# Implement following functionality:
# * appending new element to the end of collection
# * concatenating collections together using `+`
# * when element is addressed by index(using `[]`), user should get square of the addressed element.
# * when iterated using cycle `for`, elements should be given normally
# * user should be able to print whole collection as if it was list.

class MyNumberCollection:
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], tuple):
                for element in args[0]:
                    if not isinstance(element, int):
                        raise TypeError('MyNumberCollection supports only numbers!')
                self.items = list(args[0])
            elif isinstance(args[0], str):
                raise TypeError(f'{args[0]} - object is not a number!')
        else:
            self.items = [item for item in range(args[0], args[1], args[2])]
        print(self.items)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.items):
            tmp = self.index
            self.index += 1
            return self.items[tmp]
        else:
            raise StopIteration

    def __str__(self):
        return str(self.items)

    def append(self, number):
        if isinstance(number, int):
            self.items.append(number)
        else:
            raise TypeError(f'{type(number).__name__} is not a int number')

    def __add__(self, other):
        if isinstance(other, (list, MyNumberCollection)):
            return self.items + other

    def __radd__(self, other):
        if isinstance(other, (list, MyNumberCollection)):
            return other + self.items

    def __getitem__(self, index):
        return self.items[index] ** 2


if __name__ == '__main__':
    col1 = MyNumberCollection(0, 5, 2)
    col2 = MyNumberCollection((1, 2, 3, 4, 5))
    print(col1)
    print(MyNumberCollection((1, 2, 3, 4, 5)))
    # print(MyNumberCollection((1, 2, 3, "4", 5)))
    col1.append(1)
    # col1.append('qweqwe')
    print(col1)
    print(col1 + col2)
    print(col2 + col1)
    print(col2[4])
    for item in col1:
        print(item)
