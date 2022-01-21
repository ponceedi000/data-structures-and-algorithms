from stack_and_queues.node import Node

class Stack():
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

        self.size += 1

    def pop(self):
        try:
            temp = self.top
            self.top = self.top.next

            self.size -= 1
            return temp.value
        except:
            if self.top == None:
                return Exception

    def peek(self):
        try:
            return self.top.value
        except:
            if self.top.value == None:
                return Exception

    def is_empty(self):
        return self.top == None
