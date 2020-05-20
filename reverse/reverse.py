class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # prev is set to none
        prev = None
        # current is the self.head
        current = self.head
        # run a while loop while current still has a self.head
        while(current is not None):
            # sets the next node to the current node
            next_node = current.next_node
            # sets the next node to the prev node
            current.next_node = prev
            # sets the prev node to the current node
            prev = current
            # sets the current node to the next node
            current = next_node
        # Once current is none self.head will be set to prev
        self.head = prev
