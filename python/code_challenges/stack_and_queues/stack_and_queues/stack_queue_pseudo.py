from inspect import stack
from stack_and_queues.stack import Stack

class Psuedo_queue():
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()



    def enqueue(self, value):
        self.stack_1.push(value)

    def dequeue(self):
        if not self.stack_1.is_empty():
            while self.stack_1.size > 0:
                self.stack_2.push(self.stack_1.pop())
            res = self.stack_2.pop()
            while self.stack_2.size > 0:
                self.stack_1.push(self.stack_2.pop())
        return res
