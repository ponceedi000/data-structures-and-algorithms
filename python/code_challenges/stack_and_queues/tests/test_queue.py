from stack_and_queues.queue import Queue
import pytest

# TEST EIGHT - Can successfully enqueue into a queue
def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    actual = queue.rear.value
    expected = 1
    assert actual == expected

# TEST NINE - Can successfully enqueue multiple values into a queue
def test_enqueue_multiple_values():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual = queue.rear.value
    expected = 3
    assert actual == expected

# TEST TEN - Can successfully dequeue out of a queue the expected value
