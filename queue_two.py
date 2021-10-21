class Queue:
    def __init__(self):
        self.store_array = []
        self.index = -1

    def enqueue(self, data):
        self.store_array.append(data)
        self.index += 1

    def dequeue(self):
        value = self.store_array[self.index]
        del(self.store_array[self.index])
        self.index -= 1
        return value

    def size(self):
        return self.store_array.__len__()

    def __str__(self):
        return "queue two: "+self.store_array.__str__()
