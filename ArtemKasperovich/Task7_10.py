def endless_generator():
    start = 1
    while True:
        yield start
        start += 2


gen = endless_generator()
while True:
    print(next(gen))
