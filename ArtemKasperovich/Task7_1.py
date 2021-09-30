# Task 7.1
# Implement class-based context manager for opening and working with file, including handling exceptions.
# Do not use 'with open()'. Pass filename and mode via constructor.
class NewOpen:
    def __init__(self, path, mode='r+'):
        self.path = path
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.path, self.mode)
        except ValueError as value_error:
            print(f'{value_error}:Please enter a correct mode')
        except FileNotFoundError as file_error:
            print(f"{file_error}: Enter a correct path")
        else:
            return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            file.close()
        else:
            print(f'Class_error: "{exc_type},\n'
                  f'Value: {exc_val},\n'
                  f'Traceback: {exc_tb}')
        return True


with NewOpen('./111111.txt', 'qqwq') as file:
    print(file.read())
