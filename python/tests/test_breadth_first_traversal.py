from code_challenges.trees.node import Node
from code_challenges.trees.breadth_first_traversal import breadth_first
from code_challenges.trees.binary_tree import BinaryTree

def test_breadth_first():
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)
    root = BinaryTree(node)
    assert breadth_first(root) == [1,2,3,4,5]
