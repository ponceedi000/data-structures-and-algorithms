def breadth_first(tree):
    queue_list = []
    values = []
    if tree.root:
        queue_list.insert(0, tree.root)
    while queue_list:
        node = queue_list.pop()
        values.append(node.value)
        if node.left:
            queue_list.insert(0, node.left)
        if node.right:
            queue_list.insert(0, node.right)
    return values

# BELOW IS AN OLDER VERSION. DUE TO IMPORT ISSUES, THE ABOVE CODE BLOCK IS WHAT I HAD TO USE TO RUN PYTEST

# def breadth_first(tree):
#     list = []
#     breadth = Queue()
#     if tree.root is None:
#         return list

#     breadth.enqueue(tree.root)

#     while not breadth.is_empty():
#         dequeue = breadth.dequeue()
#         list.append(dequeue.value)

#         if dequeue.left:
#             breadth.enqueue(dequeue.left)

#         if dequeue.right:
#             breadth.enqueue(dequeue.right)

#         return list
