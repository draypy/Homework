# Task 6.1
# Implement a Counter class which optionally accepts the start value and the counter stop value.
# If the start value is not specified the counter should begin with 0.
# If the stop value is not specified it should be counting up infinitely.
# If the counter reaches the stop value, print "Maximal value is reached."
# Implement to methods: "increment" and "get"


class Counter:

    def __init__(self, start=0, stop=None):
        self.start = start
        self.stop = stop

    def increment(self):
        if self.start == self.stop:
            raise Exception("Maximal value is reached.")
        self.start += 1

    def get(self):
        return self.start

    def __repr__(self):
        return f"{self.__class__.__name__}(start={self.start}, stop={self.stop})"

if __name__ == '__main__':
    c = Counter(42)
    c.increment()
    c.increment()
    print(c.get())
    c.increment()
    c.increment()
    print(c.get())

    c = Counter()
    c.increment()
    c.increment()
    print(c.get())
    c.increment()
    c.increment()
    print(c.get())

    c = Counter(42, 43)
    c.increment()
    print(c.get())
    c.increment()
