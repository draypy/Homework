# Implement decorator with context manager support for writing execution time to log-file.
# See contextlib module.
from contextlib import ContextDecorator
from datetime import datetime


class my_decorator(ContextDecorator):
    def __enter__(self):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n'
        with open('log.txt', 'a') as log:
            log.writelines(now)
        return self

    def __exit__(self, *exc):
        return True


@my_decorator()
def function():
    print("Let's go to check log.txt file")


function()
