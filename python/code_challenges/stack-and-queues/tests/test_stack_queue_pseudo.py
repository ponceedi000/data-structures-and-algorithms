from stack_and_queues.stack_queue_pseudo import Psuedo_queue
from stack_and_queues.stack import Stack
import pytest

def test_enqueue():
    stack_queue = Psuedo_queue()
    stack_queue.enqueue(1)
    actual = stack_queue.stack_1.peek()
    expected = 1
    assert actual == expected

def test_enqueue_multiple_values():
    stack_queue = Psuedo_queue()
    stack_queue.enqueue(1)
    stack_queue.enqueue(2)
    stack_queue.enqueue(3)
    actual = stack_queue.stack_1.peek()
    expected = 3
    assert actual == expected

def test_enqueue_multiple_values():
    stack_queue = Psuedo_queue()
    stack_queue.enqueue(1)
    stack_queue.enqueue(2)
    stack_queue.enqueue(3)
    actual = stack_queue.stack_1.peek()
    expected = 3
    assert actual == expected

def test_dequeue_one_value():
    stack_queue = Psuedo_queue()
    stack_queue.enqueue(1)
    stack_queue.enqueue(2)
    stack_queue.enqueue(3)
    stack_queue.enqueue(4)
    actual = stack_queue.dequeue()
    expected = 1
    assert actual == expected
