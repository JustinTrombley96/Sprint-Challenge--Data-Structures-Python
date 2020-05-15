# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.data = []



#     def append(self, item):
#         # Should add the given element to the buffer.
#         self.data.append(item)
#         if len(self.data) == self.capacity:
#             self.current = 0
#             self.__class__ = RingBufferFull
        
#     def get(self):
#         # Returns all of the elements in the buffer 
#         # in a list in their given order
#         return self.data
# class RingBufferFull:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.data = []
#     def append(self, item):
#         self.current = 0
#         self.data[self.current] = item
#         self.current=(self.current + 1) % self.capacity
#     def get(self):
#         return self.data[self.current:]+self.data[:self.current]



# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.data = []



#     def append(self, item):
#         # Should add the given element to the buffer.
#         self.data.append(item)
#         if len(self.data) == self.capacity:
#             self.current = 0
#             self.data[self.current] = item
#             self.current=(self.current + 1) % self.capacity
     

        
#     def get(self):
#         # Returns all of the elements in the buffer 
#         # in a list in their given order
#         return self.data


        

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.data = []
        self.final_current = 0



    def append(self, item):
        # Should add the given element to the buffer.
        
        if len(self.data) == self.capacity:
            self.current = 0
            if self.final_current is not 4:
                self.data.pop(self.final_current)
                self.data.insert(self.final_current, item)
                self.final_current += 1
        elif len(self.data) != self.capacity:
            self.current += 1
            self.data.append(item)

     

        
    def get(self):
        # Returns all of the elements in the buffer 
        # in a list in their given order
        return self.data