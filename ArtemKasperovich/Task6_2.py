# Task 6.2
# Implement custom dictionary that will memorize 10 latest changed keys.
# Using method "get_history" return this keys.


class HistoryDict:
    def __init__(self, new_dict):
        self.new_dict = new_dict
        self.memory = []

    def set_value(self, new_key, new_value):
        if new_key in self.new_dict:
            if new_value in self.new_dict.values():
                return self.new_dict
            self.new_append(self.memory, new_key)
            self.new_dict[new_key] = new_value
            return self.new_dict
        self.new_dict[new_key] = new_value
        self.new_append(self.memory, new_key)

    def get_history(self):
        return self.memory

    @staticmethod
    def new_append(memory: list, key):
        if key in memory:
            memory.pop(memory.index(key))
            memory.append(key)
            return memory
        if len(memory) == 10:
            if key in memory:
                memory.pop(memory.index(key))
                memory.append(key)
                return memory
            memory.pop(0)
            memory.append(key)
        else:
            memory.append(key)


if __name__ == '__main__':
    x = HistoryDict({"foo": 42})
    print(x)
    x.set_value("foo", 23)
    print(x.get_history())
    x.set_value('111', 1)
    x.set_value('1', 'value')
    print(x.get_history())
    x.set_value('2', 'val11ue')
    print(x.get_history())
    x.set_value('1', 'val1ue')
    print(x.get_history())
    x.set_value('2', 'valu1e')
    print(x.get_history())
