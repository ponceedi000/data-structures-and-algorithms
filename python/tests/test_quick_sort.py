from code_challenges.quick_sort.quick_sort import quick_sort
import pytest
def test_sample():
    list = [8,4,23,42,16,15]
    size = len(list)
    actual = quick_sort(list, 0, size -1)
    expected = [4,8,15,16,23,42]
    assert list == expected

def test_reverse_sorted():
    list = [20,18,12,8,5,-2]
    size = len(list)
    actual = quick_sort(list, 0, size -1)
    expected = [-2,5,8,12,18,20]
    assert list == expected

def test_few_uniques():
    list = [5,12,7,5,5,7]
    size = len(list)
    actual = quick_sort(list, 0, size -1)
    expected = [5,5,5,7,7,12]
    assert list == expected

def test_nearly_sorted():
    list = [2,3,5,7,13,11]
    size = len(list)
    actual = quick_sort(list, 0, size -1)
    expected = [2,3,5,7,11,13]
    assert list == expected
