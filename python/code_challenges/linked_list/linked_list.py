class Node:
    def __init__(self, value, next =None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        current = self.head
        ll_output = ""
        if current == None:
            ll_output = '{NONE}'
        else:
            # struggled with formating our values into the required output. Colloborated with Brandon Mizutani to solve this problem
            # Looked up .format documents from w3 schools
            ll_output += '{}{}{}'.format("{ ", current.value, " }")
            while current.next:
                ll_output += ' -> {}{}{}'.format('{ ', current.next.value, ' }')
                current = current.next
            ll_output += f' -> NONE'
            return ll_output
