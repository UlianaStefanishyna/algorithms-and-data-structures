from item import Item
from linked_list import LinkedList, convert_arraylist_to_linked_list

"""
Dequeue. A double-ended queue or deque (pronounced “deck”) is a generalization of a stack 
and a queue that supports adding and removing items from either the front or the back of the data structure.
@link: https://coursera.cs.princeton.edu/algs4/assignments/queues/specification.php
"""


class Deque:

    def __init__(self, array):
        self.data: LinkedList = convert_arraylist_to_linked_list(array)

    def is_empty(self) -> bool:
        return self.data.size() == 0 if self.data else True

    def size(self) -> int:
        return self.data.size() if self.data else 0

    def add_first(self, item):
        self.data.insert_at_the_beginning(Item(item))

    def add_last(self, item):
        self.data.insert_at_position(position=self.size(), data=item)

    def remove_first(self) -> Item:
        return self.data.remove_at_the_beginning()

    def remove_last(self) -> Item:
        return self.data.remove_at_position(self.size()-1)


if __name__ == '__main__':
    dq: Deque = Deque(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
    assert dq.size() == 9
    dq.add_last('U')
    dq.data.print_linked_list()
    assert dq.size() == 10
    dq.add_first('P')
    assert dq.size() == 11
    assert dq.remove_last() == 'U'
    assert dq.size() == 10
    assert dq.remove_first() == 'P'
