from code_challenges.linked_list_insertions.linked_list_insertions import LinkedList, Node
import pytest

def test_node_instance():
    node = Node(1, None)
    assert node.next == None
    assert node.value == 1

def test_node_instance_fail():
    node = Node(1, None)
    assert node.next != node
    assert node.value != 2

def test_linked_list():
    node = Node(1, None)
    ll = LinkedList(node)
    assert ll.head == node


