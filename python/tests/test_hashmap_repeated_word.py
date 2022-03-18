from code_challenges.hashmap_repeated_word.hashmap_repeated_word import hashmap_repeated_word


def test_hashmap_repeated_word_typical_case():
    text = "it was a cold and windy day that lead to a saturday"
    assert hashmap_repeated_word(text) == "a"


def test_hashmap_repeated_word_with_punctuation():
    text = "It was a cold and windy day, that lead to a saturday!"
    assert hashmap_repeated_word(text) == "a"


def test_hashmap_repeated_word_case_insensitive():
    text = "It was! a Cold and WindY day, that lead tO a Saturday!"
    assert hashmap_repeated_word(text) == "a"


def test_hashmap_repeated_word_first_repeat():
    text = "It was a cold and windy day, that lead to a very cold saturday!"
    assert hashmap_repeated_word(text) == "a"


def test_hashmap_repeated_word_last_repeat():
    text = "Sally sold seashells by the seashore. Good for you Sally."
    assert hashmap_repeated_word(text) == "sally"


def test_hashmap_repeated_word_empty():
    text = ""
    assert hashmap_repeated_word(text) == None


def test_hashmap_repeated_word_last_repeat_and_punctuation():
    text = "sally sold seashells by the seashore good for you sally."
    assert hashmap_repeated_word(text) == 'sally'


def test_hashmap_repeated_word_punctuation_only():
    text = "%^!#)_= 1234.#$!*(+= %^!#)_= ."
    assert hashmap_repeated_word(text) == None


def test_hashmap_repeated_word_hyphen_dashes():
    text = "sal-ly sold seashells by the seashore. good for you sal-ly"
    assert hashmap_repeated_word(text) == "sal"
