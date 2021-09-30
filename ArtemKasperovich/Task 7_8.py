# Implement your custom iterator class called MySquareIterator
# which gives squares of elements of collection it iterates through.
class MyIterator:
    def __init__(self, collection):
        self.collection = collection

    def __iter__(self):
        self.iter = 0
        return self

    def __next__(self):
        if self.iter < len(self.collection):
            square = self.collection[self.iter] ** 2
            self.iter += 1
            return square
        else:
            raise StopIteration

if __name__ == "__name__":
    las = [4, 5, 6]
    iterator = MyIterator(las)
    for ite in iterator:
        print(ite)
