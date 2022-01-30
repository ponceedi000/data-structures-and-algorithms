from stack_and_queues.stack import Stack

class AnimalShelter():
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, animal):
        if animal != 'dog' and animal != 'cat':
            return None
        while self.in_stack.top:
            newValue = self.in_stack.pop()
            self.out_stack.push(newValue)

        self.in_stack.push(animal)

        while self.in_stack.top:
            newValue = self.out_stack
            self.in_stack.push(newValue)

    # def check_pref(self, pref):
    #     if pref == None:
    #         return None
    #     elif pref == 'dog':
    #         return 'dog'
    #     elif pref == 'cat':
    #         return 'cat'

    def dequeue(self, pref):
        if pref != 'dog' and pref != 'cat':
            return None
        elif pref == 'cat' and self.in_stack.top == 'cat':
            self.in_stack.pop()
        elif pref == 'dog' and self.in_stack.top == 'dog':
            self.in_stack.pop()



        # if pref != 'dog' and pref != 'cat':
        #     return None
        # while not self.in_stack.is_empty():
        #     temp = self.in_stack.pop()
        #     if temp == pref:
        #         self.out_stack.push(temp)
        #         return self.out_stack.pop()



