class Queue:

    def __init__(self):
        self.store_array = []
        self.index = -1

    def enqueue(self, data):
        self.index += 1
        self.store_array.append(data)

    def dequeue(self):
        if self.index >= 0:
            value = self.store_array[0]
            del(self.store_array[0])
            self.index -= 1
            return value
        return None

    def size(self):
        return self.store_array.__len__()

    def index_len(self):
        return self.index

    def __str__(self):
        return self.store_array
