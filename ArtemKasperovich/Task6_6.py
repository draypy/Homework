# Task 4.6
# A singleton is a class that allows only a single instance of itself to be created
# and gives access to that created instance.
# Implement singleton logic inside your custom class using a method to initialize class instance.

class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


a = Singleton(123123)
b = Singleton(99999)

print(a is b)
