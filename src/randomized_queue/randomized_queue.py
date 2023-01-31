from item import Item
from random import randint, sample
from linked_list import LinkedList, convert_arraylist_to_linked_list
"""
Randomized queue. A randomized queue is similar to a stack or queue, except that the item 
removed is chosen uniformly at random among items in the data structure.
Your randomized queue implementation must support each randomized queue operation 
in constant amortized time. That is, any intermixed sequence of m randomized queue operations 
(starting from an empty queue) must take at most cm steps in the worst case, for some constant c.
@link: https://coursera.cs.princeton.edu/algs4/assignments/queues/specification.php
"""


class RandomizedQueue:

    def __init__(self, length, array):
        if length > len(array):
            raise Exception
        self.data: LinkedList = convert_arraylist_to_linked_list([array[i] for i in sample(range(len(array)), length)])

    def is_empty(self) -> bool:  # O(1)
        return self.size() == 0 if self.data else True

    def size(self) -> int:  # O(1)
        return self.data.size() if self.data else 0

    # add item
    def enqueue(self, item):  # O(1)
        self.data.insert_at_the_beginning(Item(item))

    # remove random item
    def dequeue(self) -> Item:  # O(m)
        index_to_remove = randint(1, self.data.size())
        return self.data.remove_at_position(index_to_remove-1)

    def sample(self) -> Item:  # O(m)
        index_to_peek = randint(1, self.data.size())
        return self.data.get_at_position(index_to_peek-1)


if __name__ == '__main__':
    rq: RandomizedQueue = RandomizedQueue(4, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
    assert rq.size() == 4

    print(rq.sample())

    rq.enqueue('U')
    assert rq.data.get_at_position(0) == 'U'
    assert rq.size() == 5

    dequeued_item = rq.dequeue()
    assert rq.size() == 4
