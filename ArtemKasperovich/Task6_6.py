# Task 4.6
# A singleton is a class that allows only a single instance of itself to be created
# and gives access to that created instance.
# Implement singleton logic inside your custom class using a method to initialize class instance.

class Singleton:
    __instance = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            instance = super().__new__(cls)
            cls.__instance[cls] = instance
        return cls.__instance


a = Singleton(123123)
b = Singleton(99999)
c = Singleton(1)
d = Singleton(2)


if __name__ == '__main__':
    print(id(a), id(b), id(c), id(d), sep='\n')
