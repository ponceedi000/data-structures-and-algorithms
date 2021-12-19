# Singly Linked List
- > "A linked list is created by using the node class we studied in the last chapter. We create a Node object and create another class to use this ode object. We pass the appropriate values through the node object to point the to the next data elements." [tutorialspoint.com](https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm)

- PR: [https://github.com/ponceedi000/data-structures-and-algorithms/pull/20](https://github.com/ponceedi000/data-structures-and-algorithms/pull/20)

## Challenge

### Node
- Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

### Linked List
- Create a Linked List class
- Within your Linked List class, include a head property.
  * Upon instantiation, an empty Linked List should be created.
- The class should contain the following methods
  * insert
    * Arguments: value
    * Returns: nothing
    * Adds a new node with that value to the head of the list with an O(1) Time performance.
- includes
  * Arguments: value
  * Returns: Boolean
    * Indicates whether that value exists as a Node’s value somewhere within the list.
- to string
  * Arguments: none
  * Returns: a string representing all the values in the Linked List, formatted as:
  * `"{ a } -> { b } -> { c } -> NULL"`
- Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

### Solar System Exploration, 1950s – 1960s

- [x] Can successfully instantiate an empty linked list
- [x] Can properly insert into the linked list
- [x] The head property will properly point to the first node in the linked list
- [x] Can properly insert multiple nodes into the linked list
- [x] Will return true when finding a value within the linked list that exists
- [x] Will return false when searching for a value in the linked list that does not exist
- [x] Can properly return a collection of all the values that exist in the linked list

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- I approached this code challenge with a test driven mindset. I first ran very simple tests as a 'proof of life' before getting into the code. While coding, i broke everything into smaller steps. I worked each method one-by-one, each method having a minimum of one test before progressing foward. Once my code was complete, i went through each method again with additional tests to ensure functionality and efficiency of my code. Lastly, i added a try/except block to each method to ensure errors were being handled the right way(This is import because we are human and mistakes are part of our nature. It is important to have error handling in case of future bugs appear that weren't covered in my testing suite.)

## Time Log
- Started at: aprox. 3pm
- Ended at: aprox. 7pm
- Initial time expected to complete: 3 hours
- final time to complete: approx. 4 hours

## Credits and Colaborations
- Alex Payne, and Brandon Mizutani
- [tutorialspoint.com | LinkedLists docs](https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm)
- [w3 Schools | .format()](https://www.w3schools.com/python/ref_string_format.asp)
