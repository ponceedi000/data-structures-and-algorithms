from code_challenges.linked_list.linked_list import LinkedList, Node
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

def test_includes_node_value():
    ll = LinkedList()
    ll.insert("one")
    ll.insert("two")
    ll.insert("three")
    ll.insert("four")
    ll.insert("five")
    ll.insert("six")
    assert ll.includes("six") == True

def test_does_not_includes_node_value():
    ll = LinkedList()
    ll.insert("one")
    ll.insert("two")
    ll.insert("three")
    ll.insert("four")
    ll.insert("five")
    ll.insert("six")
    assert ll.includes("seven") == False
