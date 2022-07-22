def depth_first(graph, start):
    list = []
    visited = set()
    stack = Stack()

    while stack:
        head = stack.pop()
        if stack in visited:
            continue

        yield head
        visited.add(head)

        for child in graph[head]:
            stack.append(child)



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

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
