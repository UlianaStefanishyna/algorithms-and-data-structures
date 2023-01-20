from linked_list.node import Node


class LinkedList(object):
    def __init__(self, head: Node = None):
        self.head = head
        self.count = 0 if head is None else 1

    def append_item(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            curr_node = self.head
            prev_node = None
            while curr_node:
                prev_node = curr_node
                curr_node = curr_node.next_node
            prev_node.next_node = node
        self.count += 1

    def insert_at_position(self, data, position):
        if position > self.size():
            raise Exception(f'LinkedList length is {self.size()}, hence position doesn\'t exist. '
                            f'To append use index {self.size()}')

        if position < 0:
            raise Exception('Position cannot be negative')

        new_node = Node(data)
        if position == 0:
            self.insert_at_the_beginning(new_node)
            self.count += 1
            return

        curr_index = 0
        curr_node: Node = self.head
        while curr_index + 1 < position:
            curr_node = curr_node.next_node
            curr_index += 1
        tmp: Node = curr_node.next_node
        curr_node.next_node = new_node
        new_node.next_node = tmp
        self.count += 1
        return self.head

    def insert_at_the_beginning(self, node):
        curr_head = self.head
        self.head = node
        self.head.next_node = curr_head
        return self.head

    def size(self):
        return self.count

    def get_at_position(self, position):
        if position > self.size() - 1:
            raise Exception(f'LinkedList length is {self.size()}, hence position {position} doesn\'t exist.')

        if position < 0:
            raise Exception('Position cannot be negative')

        curr_index = 0
        curr_node = self.head

        while curr_index < position:
            curr_node = curr_node.next_node
            curr_index += 1
        return curr_node.data

    def remove_at_position(self, position):
        if position > self.size() - 1:
            raise Exception(f'LinkedList length is {self.size()}, hence position {position} doesn\'t exist.')

        if position < 0:
            raise Exception('Position cannot be negative')

        if position == 0:
            self.remove_at_the_beginning()

        curr_index = 0
        curr_node = self.head
        while curr_index + 1 < position:
            curr_node = curr_node.next_node
            curr_index += 1
        curr_node.next_node = curr_node.next_node.next_node
        self.count -= 1

    def remove_at_the_beginning(self):
        curr_head = self.head
        next_node = curr_head.next_node
        self.head = next_node
        self.count -= 1

    def print_linked_list(self):
        print()
        temp = self.head
        while temp:
            print(temp.data, ', ', end='')
            temp = temp.next_node
        print("")


def convert_arraylist_to_linked_list(array_list: list):
    linked_list = LinkedList()
    for item in array_list:
        linked_list.append_item(item)
    return linked_list
