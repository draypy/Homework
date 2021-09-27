#  Task 4.4
# Create hierarchy out of birds.
# Implement 4 classes:
# * class `Bird` with an attribute `name` and methods `fly` and `walk`.
# * class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value.
# Implement the method `eat` which will describe its typical ration.
# * class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
# Add same "eat" method but with other implementation regarding the swimming bird tastes.
# * class `SuperBird` which can do all of it: walk, fly, swim and eat.
# But be careful which "eat" method you inherit.
# Implement str() function call for each class.

class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return f'{self.name} bird can fly'

    def walk(self):
        return f'{self.name} bird can walk'

    def __str__(self):
        return f"Name the bird - {self.name}"


class FlyingBird(Bird):

    def __init__(self, name, ration='mouse'):
        super().__init__(name)
        self.name = name
        self.ration = ration

    def eat(self):
        return f'It eats mostly {self.ration}'

    def __str__(self):
        return f"Name the bird - {self.name}"


class NonFlyingBird(Bird):
    def __init__(self, name, ration='plankton'):
        super().__init__(name)
        self.name = name
        self.ration = ration

    def swim(self):
        return fr'{self.name} can swim'

    def eat(self):
        return f'It eats mostly {self.ration}'

    def __str__(self):
        return f"Name the bird - {self.name}"


class SuperBird(FlyingBird, NonFlyingBird):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"Name the bird - {self.name}"


if __name__ == '__main__':
    b = Bird("Any")
    print(b.walk())
    print(b)
    p = NonFlyingBird("Penguin")
    print(p.swim())
    # print(p.fly())
    print(p)
    c = FlyingBird('Canary')
    print(c.eat())
    print(c)
    s = SuperBird('Gull')
    print(s.name)
    print(s.eat())
    print(s.swim())
    print(s.walk())
    print(s.fly())
    print(SuperBird.__mro__)
    print(s)

