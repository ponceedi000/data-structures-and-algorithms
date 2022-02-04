from trees.node import Node

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
        try:
            temp = self.front
            self.front = temp.next
            temp.next = None
            return temp.value
        except:
            return Exception('Cannot dequeue if empty!')

    def peek(self):
        try:
            return self.front.value
        except:
            raise Exception('Cannot peek an empty queue. Shame.')

    def is_empty(self):
        return self.front == None

