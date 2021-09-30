# 7.6
# Create console program for proving Goldbach's conjecture. Program accepts number for input and print result.
# For pressing 'q' program succesfully close. Use function from Task 5.5
# for validating input, handle all exceptions and print user friendly output.

def prime(check_prime):
    d = 2
    while d * d <= check_prime and check_prime % d != 0:
        d += 1
    return d * d > check_prime


def even(n):
    try:
        if isinstance(int(n), int):
            n = int(n)
            if n % 2 == 0 and n > 3:
                return True
            return False
    except ValueError:
        return False


number = input('Enter a number: ')
while True:
    if even(number):
        number = int(number)

        if number == 4:
            print(2, 2)
            number = input('Enter a new number: ')
        else:
            d = 3
            while not prime(d) or not prime(number - d):
                d += 1
            print(d, number - d)
            number = input('Enter a number: ')
            continue
    elif len(number) == 1 and number == 'q':
        break
    else:
        number = input('Enter a new number: ')
        continue

