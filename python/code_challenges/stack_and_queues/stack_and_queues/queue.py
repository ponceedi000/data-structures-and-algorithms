from stack_and_queues.node import Node

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self, value):
        new_node = Node(value)

        if self.front == None:
           self.front = self.rear
           self.rear = new_node

        self.rear.next = new_node
        self.rear = new_node


    def dequeue(self):
        temp = self.front
        self.front = self.front.next
        temp.next = None

        return temp.value


    def peek(self):
        return self.front.value

    def is_empty(self):
        return self.front == None

