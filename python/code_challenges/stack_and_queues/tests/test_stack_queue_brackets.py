from stack_and_queues.stack_queue_brackets import multi_bracket_validation
import pytest


def test_true():
    stack = multi_bracket_validation

    actual = stack.push('[[]]')
    expected = True
    assert actual == expected
