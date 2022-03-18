# Hashtables
- [PR Link](https://github.com/ponceedi000/data-structures-and-algorithms/pull/35)

> "Hash tables are a type of data structure in which the address or the index value of the data element is generated from a hash function. That makes accessing the data faster as the index value behaves as a key for the data value. In other words Hash table stores key-value pairs but the key is generated through a hashing function." - [tutorialspint](https://www.tutorialspoint.com/python_data_structure/python_hash_table.htm)

## Challenge
Implement a Hashtable Class with the following methods:

- set
  * Arguments: key, value
  * Returns: nothing
  * This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
  * Should a given key already exist, replace its value from the value argument given to this method.
- get
  * Arguments: key
  * Returns: Value associated with that key in the table
  * contains
  * Arguments: key
  * Returns: Boolean, indicating if the key exists in the table already.
- keys
  * Returns: Collection of keys
- hash
  * Arguments: key
  * Returns: Index in the collection for that key

## Approach & Efficiency
- Instead of writing all of my code first followed by testing, I decided write tests per new class method. This broke everything down into smaller steps which helped a lot

- BigO
  * Space: O(1)
  * Time: O(1)

## API
- hash
  * Arguments: key
  * Returns: Index in the collection for that key
- Add
  * Arguments: key, value
  * Returns: nothing
  * This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
  * Should a given key already exist, replace its value from the value argument given to this method.

- get
  * Arguments: key
  * Returns: Value associated with that key in the table

- contains
  * Arguments: key
  * Returns: Boolean, indicating if the key exists in the table already.


## Credits and Colaborations
- [Hash Table implementation in Python [Data Structures & Algorithms]](https://blog.chapagain.com.np/hash-table-implementation-in-python-data-structures-algorithms/#:~:text=Standard%20Implementation&text=Python's%20built%2Din%20%E2%80%9Chash%E2%80%9D,be%2020%2C%20and%20so%20on.)
- [Python - Hash Table](https://www.tutorialspoint.com/python_data_structure/python_hash_table.htm)
- [Introduction to Hash Tables and Dictionaries](https://www.youtube.com/watch?v=sfWyugl4JWA)
- [Hash Table in Data Structure: Python Example](https://www.guru99.com/hash-table-data-structure.html)

