from code_challenges.insertion_sort.insert_sort import insertion_sort
import pytest

def test_insertion_sort_sample():
    list = [8, 4, 23, 42, 16, 15]
    actual = insertion_sort(list)
    assert actual == [4, 8, 15, 16, 23, 42]

def test_reverse_sorted():
    list = [20, 18, 12, 8, 5, -2]
    actual = insertion_sort(list)
    assert actual == [-2, 5, 8, 12, 18, 20]

def test_few_uniques():
    list = [5, 12, 7, 5, 5, 7]
    actual = insertion_sort(list)
    assert actual == [5, 5, 5, 7, 7, 12]

def test_nearly_sorted():
    list = [2, 3, 5, 7, 13, 11]
    actual = insertion_sort(list)
    assert actual == [2, 3, 5, 7, 11, 13]
