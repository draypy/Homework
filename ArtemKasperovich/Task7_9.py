class EvenRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.start = self.check(self.start, self.end)
    @staticmethod
    def check(start, end):
        if start < end and start % 2 != 0:
            start += 1
            return start
        return start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start % 2 == 0 and self.start <= self.end:
            tmp = self.start
            self.start += 2
            return tmp
        else:
            print('Out of members!')
            raise StopIteration
    def __str__(self):
        return self.start + ' '



if __name__ == "__main__":
    er1 = EvenRange(7, 11)
    print(next(er1))
    print(next(er1))
    print(next(er1))

    er2 = EvenRange(3, 14)
    for number in er2:
        print(number)