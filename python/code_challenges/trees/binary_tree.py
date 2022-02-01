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



class BinarySearchTree(BinaryTree):

    def __init__(self, root=None):
        self.root = root

    # This methods logic was created referencing an article from cppsecrets.com

    def add(self, value):
        def walk(root):
            if value < root.value:
                if root.left is None:
                    root.left = Node(value)
                else:
                    walk(root.left)
            else:
                if root.right is None:
                    root.right = Node(value)
                else:
                    walk(root.right)
        walk(self.root)

    # Code inspired by Taylor White from class code review
    def contains(self, value):
      if self.root.value == value:
        return True
      else:
        def walk(root, value):
          if root.value == value:
            return True
          elif value < root.value:
              return walk(root.left, value)
          elif value > root.value:
              return walk(root.right, value)
          else:
            return False
        return walk(self.root, value)

