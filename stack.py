class Stack:

    def __init__(self):
        self.store_array = []
        self.index = 0

    def add(self, data):
        self.store_array.append(data)
        self.index += 1

    def pop(self):
        if self.index > 0:
            value = self.store_array[self.index-1]
            del(self.store_array[self.index-1])
            self.index -= 1

            return value
        else:
            return None

    def size(self):
        return self.store_array.__len__()

    def index_len(self):
        return self.index

    def __str__(self):
        return self.store_array
