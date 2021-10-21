class StackTwo:

    def __init__(self):
        self.store_array = []

    def append(self, data):
        self.store_array.append(data)

    def pop(self):
        return self.store_array.pop()

    def __str__(self):
        return self.store_array
