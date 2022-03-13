# class Node:
#     def __init__(self, key, value, next=None):
#         self.key = key
#         self.value = value
#         self.next = None
# I PLAN ON FINDING A WAY TO IMPLEMENT LINKED-LISTS IN THE NEAR FUTURE


class Hashtable:

    def __init__(self, size=1024):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]

        # Initializer

    def hash(self, key):
        sum = 0
        for ch in key:
             sum += ord(ch)

        primed = sum * 11
        index = primed % self.size

        return index

        # hash
        # Arguments: key
        # Returns: Index in the collection for that key


    def add(self, key, value):
        index = self.hash(key)
        is_found = False

        for i, element in enumerate(self.buckets[index]):
            if len(element) == 2 and element[0] == key:
                self.buckets[index][i] = (key, value)
                is_found = True
                break
        if not is_found:
            self.buckets[index].append((key, value))

        # Add
        # Arguments: key, value
        # Returns: nothing
        # This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
        # Should a given key already exist, replace its value from the value argument given to this method.

    def get(self, key):
        index = self.hash(key)
        for element in self.buckets[index]:
            if element[0] == key:
                return element[1]

        # get
        # Arguments: key
        # Returns: Value associated with that key in the table

    def contains(self, key):
        index = self.hash(key)
        for element in self.buckets[index]:
            if element[0] == key:
                return True

        return False

        # contains
        # Arguments: key
        # Returns: Boolean, indicating if the key exists in the table already.


    def keys():
        pass
    # COULD NOT FIND ANY ABOUT THE IMPLEMNTATION OF keys()

        # keys
        # Returns: Collection of keys
