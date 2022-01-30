from code_challenges.trees.node import Node

class BinaryTree:
    def __init__(self, root=None):
        self.root = root


# AFTER WRITING LOGIC FOR PRE ORDER METHOD, I CAME TO REALIZATION THAT THE OTHER METHODS
# WOULD BE WRITTEN VERY SIMILARY
# I HAD TO SLIGHT MODIFY LOGIC BASED OF THE METHODS TRAVERSAL FLOW


    def pre_order(self):
# root > left > right
        values = []
        if self.root == None:
            raise Exception('Tree is empty')

        def walk(root):
            if root:
                values.append(root.value)
                walk(root.left)
                walk(root.right)
        walk(self.root)
        return values

    def in_order(self):
# left > root > right
        values = []
        if self.root == None:
            raise Exception('Tree is empty')

        def walk(node):
            if node:
                walk(node.left)
                values.append(node.value)
                walk(node.right)
        walk(self.root)
        return values

    def post_order(self):
# left > right > root
        values = []
        if self.root == None:
            raise Exception('Tree is empty')

        def walk(node):
            if node:
                walk(node.left)
                walk(node.right)
                values.append(node.value)
        walk(self.root)
        return values


# class BinarySearchTree:

# STILL WORKING ON ADD METHOD

    # def add(self, value):
    #     def walk(node):
    #         if value < node.value:
    #             if node.left == None:
    #                 node.left = Node(value)
    #             else:
    #                 walk(node.left)
    #     walk(self.root)
