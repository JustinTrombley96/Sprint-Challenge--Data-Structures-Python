class RingBuffer:
    def __init__(self, capacity):
        self.capacity = 5
        self.data = ['a', 'b', 'c', 'd', 'e']


    def append(self, item):
        # Should add the given element to the buffer.
        self.data.pop(0)
        self.data.append(item)

    def get(self):
        # Returns all of the elements in the buffer 
        # in a list in their given order
        return self.data