import time


def endless_generator():
    first = 0
    second = 1
    while True:
        yield first + second
        first, second = second, first + second


gen = endless_generator()
while True:
    print(next(gen))
    time.sleep(0.3) #pc_will_survive
