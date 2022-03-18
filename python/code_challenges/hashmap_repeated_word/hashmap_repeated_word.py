from code_challenges.hash_tables.hash_table import Hashtable

def hashmap_repeated_word(string):
    word_tracker = ""
    hash = Hashtable()

    for ch in string:
        lower_ch = ch.lower()
        if ord(lower_ch) in range(ord("a"), ord("z")+1):
            word_tracker += lower_ch
        elif len(word_tracker):
            if hash.contains(word_tracker):
                return word_tracker
            else:
                hash.add(word_tracker, None)
                word_tracker = ""
    if len(word_tracker) and hash.contains(word_tracker):
        return word_tracker
    return None
