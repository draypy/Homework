# Task 7.2
# Implement context manager for opening and working with file,
# including handling exceptions with @contextmanager decorator.

from contextlib import contextmanager


@contextmanager
def open_v2(file, mode='r'):
    open_file = None
    try:
        open_file = open(file, mode)
        yield open_file
    except Exception as ex:
        print(f'{ex.__class__.__name__}:{ex}')
    finally:
        if open_file:
            open_file.close()


with open_v2("Task7_1.py", 'r1') as a:
    print(a.readline())
    print(a.read())

# with open_v2("Task1_1.py", 'r') as a:
#     print(a.readline())
