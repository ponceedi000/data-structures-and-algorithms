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

def test_insert_to_string():
    test_out_insert_to_string = LinkedList()
    test_out_insert_to_string.insert('a')
    test_out_insert_to_string.insert('b')
    test_out_insert_to_string.insert('c')
    actual = test_out_insert_to_string.head.value
    expected = 'c'
    assert actual == expected
    actual = test_out_insert_to_string.to_string()
    expected = '{ c } -> { b } -> { a } -> NONE'
    assert actual == expected
