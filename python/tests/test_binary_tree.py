from code_challenges.trees.binary_tree import BinaryTree
from code_challenges.trees.node import Node

def test_new_node():
    node = Node(123)
    actual = node.value
    expected = 123

    assert actual == expected

def test_new_node_not_working():
    node = Node(123)
    actual = node.value
    expected = 124

    assert actual != expected

def test_bt_isEmpty():
    bt = BinaryTree()

    assert bt

def test_bt_preorder():
#         apple
#      /        \
#    pear     orange

    apple = Node('apple')
    pear = Node('pear')
    orange = Node('orange')
    bt = BinaryTree(apple)
    apple.left = pear
    apple.right = orange

    assert apple.left == bt.root.left
    assert apple.right == orange
    order_list = bt.pre_order()
    assert order_list == ['apple', 'pear', 'orange']

def test_bt_preorder_not_working():
#         apple
#      /        \
#    pear     orange

    apple = Node('apple')
    pear = Node('pear')
    orange = Node('orange')
    bt = BinaryTree(apple)
    apple.left = pear
    apple.right = orange

    assert apple.left == bt.root.left
    assert apple.right == orange
    order_list = bt.pre_order()
    assert order_list != ['pear', 'apple', 'orange']
    assert order_list != ['pear', 'orange', 'apple']
    assert order_list != ['orange', 'apple', 'pear']
    assert order_list != ['orange', 'pear', 'apple']
    assert order_list != ['apple', 'orange', 'pear']

def test_bt_in_order():
#         apple
#      /        \
#    pear     orange

    apple = Node('apple')
    pear = Node('pear')
    orange = Node('orange')
    bt = BinaryTree(apple)
    apple.left = pear
    apple.right = orange

    assert apple.left == bt.root.left
    assert apple.right == orange
    order_list = bt.in_order()
    assert order_list == ['pear', 'apple', 'orange']

def test_bt_in_order_not_working():
#         apple
#      /        \
#    pear     orange

    apple = Node('apple')
    pear = Node('pear')
    orange = Node('orange')
    bt = BinaryTree(apple)
    apple.left = pear
    apple.right = orange

    assert apple.left == bt.root.left
    assert apple.right == orange
    order_list = bt.in_order()
    assert order_list != ['orange', 'pear', 'apple']
    assert order_list != ['orange', 'apple', 'pear']
    assert order_list != ['apple', 'pear', 'orange']
    assert order_list != ['apple', 'orange', 'pear']
    assert order_list != ['pear', 'orange', 'apple']

def test_bt_postorder():
#         apple
#      /        \
#    pear     orange

    apple = Node('apple')
    pear = Node('pear')
    orange = Node('orange')
    bt = BinaryTree(apple)
    apple.left = pear
    apple.right = orange

    assert apple.left == bt.root.left
    assert apple.right == orange
    order_list = bt.post_order()
    assert order_list == ['pear', 'orange', 'apple']

def test_bt_postorder_not_working():
#         apple
#      /        \
#    pear     orange

    apple = Node('apple')
    pear = Node('pear')
    orange = Node('orange')
    bt = BinaryTree(apple)
    apple.left = pear
    apple.right = orange

    assert apple.left == bt.root.left
    assert apple.right == orange
    order_list = bt.post_order()
    assert order_list != ['pear', 'apple', 'orange']
    assert order_list != ['orange', 'apple', 'pear']
    assert order_list != ['orange', 'pear', 'apple']
    assert order_list != ['apple', 'pear', 'orange']
    assert order_list != ['apple', 'orange', 'pear']

