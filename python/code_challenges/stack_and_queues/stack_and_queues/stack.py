from stack_and_queues.node import Node

class Stack():
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        try:
            temp = self.top
            self.top = self.top.next
            return temp.value
        except:
            if self.top == None:
                return Exception

    def peek(self):
        # if self.top.value == None:
        #     return Exception
        # else:
        #     return self.top.value

        try:
            return self.top.value
        except:
            if self.top.value == None:
                return Exception

    def is_empty(self):
        return self.top == None
