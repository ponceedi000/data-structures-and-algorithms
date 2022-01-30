from stack_and_queues.queue import Queue
import pytest

# TEST EIGHT - Can successfully enqueue into a queue
def test_queue_enqueue():
    queue = Queue()
    queue.enqueue(1)
    actual = queue.rear.value
    expected = 1
    assert actual == expected

# TEST NINE - Can successfully enqueue multiple values into a queue
def test_queue_enqueue_multiple_values():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual = queue.rear.value
    expected = 3
    assert actual == expected

# TEST TEN - Can successfully dequeue out of a queue the expected value
def test_queue_dequeue():
    queue = Queue()
    queue.enqueue(4)
    queue.enqueue(2)
    queue.dequeue()
    actual = queue.front.value
    expected = 4
    assert actual == expected

# TEST ELEVEN - Can successfully peek into a queue, seeing the expected value
def test_queue_peek():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(10)
    queue.enqueue(100)
    actual = queue.peek()
    expected = 1
    assert actual == expected

# TEST TWELVE - Can successfully empty a queue after multiple dequeues
def test_queue_empty_with_multiple_dequeues():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(10)
    queue.enqueue(100)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    actual = queue.front
    expected = None
    assert actual == expected

# TEST THIRTEEN - Can successfully instantiate an empty queue
def test_stack_is_empty_True():
    queue = Queue()
    # actual = queue.front
    # expected = None
    # assert actual == expected
    assert queue.is_empty() == True

# TEST FOURTEEN - Calling dequeue on empty queue raises exception
def test_queue_empty_dequeue_raise_exception():
    with pytest.raises(Exception):
        queue = Queue()
        queue.peek()


    # <--- AND --->

# TEST FOURTEEN - Calling peek on empty queue raises exception

def test_queue_empty_peek_raise_exception():
    with pytest.raises(Exception):
        queue = Queue()
        queue.peek()
