- [PR Link Here](https://github.com/ponceedi000/data-structures-and-algorithms/pull/25)

# Stacks and Queues
- A stack is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.
- Like stack, queue is a linear data structure that stores items in First In First Out (FIFO) manner. With a queue the least recently added item is removed first.

## Challenge
- Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

### Write tests to prove the following functionality:

1. Can successfully push onto a stack
2. Can successfully push multiple values onto a stack
3. Can successfully pop off the stack
4. Can successfully empty a stack after multiple pops
5. Can successfully peek the next item on the stack
6. Can successfully instantiate an empty stack
7. Calling pop or peek on empty stack raises exception
8. Can successfully enqueue into a queue
9. Can successfully enqueue multiple values into a queue
10. Can successfully dequeue out of a queue the expected value
11. Can successfully peek into a queue, seeing the expected value
12. Can successfully empty a queue after multiple dequeues
13. Can successfully instantiate an empty queue
14. Calling dequeue or peek on empty queue raises exception

## Approach & Efficiency
- First I created my Node class with two required properties (self.value and self.next). Next I decided to work on my Stack class and write the logic for each required method. Right after I coded the logic for each method, I wrote tests and made adjustments class methods until all tests were running properly/accurately.
- I then moved onto my Queue class and repeated the same process.

## API
- push
  * Arguments: value
  * adds a new node with that value to the top of the stack with an O(1) Time performance.
- pop
  * Arguments: none
  * Returns: the value from node from the top of the stack
  * Removes the node from the top of the stack
  * Should raise exception when called on empty stack
- peek
  * Arguments: none
  * Returns: Value of the node located at the top of the stack
  * Should raise exception when called on empty stack
- is empty
  * Arguments: none
  * Returns: Boolean indicating whether or not the stack is empty.
- enqueue
  * Arguments: value
  * adds a new node with that value to the back of the queue with an O(1) Time performance.
- dequeue
  * Arguments: none
  * Returns: the value from node from the front of the queue
  * Removes the node from the front of the queue
  * Should raise exception when called on empty queue
- peek
  * Arguments: none
  * Returns: Value of the node located at the front of the queue
  * Should raise exception when called on empty stack
- is empty
  * Arguments: none
  * Returns: Boolean indicating whether or not the queue is empty


### ADDITIONAL FEATURE TASKS
- Create a new class called pseudo queue. Do not use an existing Queue. Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below). Internally, utilize 2 Stack instances to create and manage the queue.
- Start Time: 7:30pm
- End Time: Pending
-
## Credits and Colaborations
- Brandon Mizutani
- Isaiah Burkes
- Alex Payne

## Resources
- [Stacks and Queues in Python](https://pynote.readthedocs.io/en/latest/DataTypes/Stack_Queue.html)
- [Queue using Stacks](https://www.geeksforgeeks.org/queue-using-stacks/)
- [Implement A Queue using Two Stacks Python](https://stackoverflow.com/questions/22430803/implement-a-queue-using-two-stacks-python)



