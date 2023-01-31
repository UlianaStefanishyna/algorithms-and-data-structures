from item import Item


class LinkedList(object):
    def __init__(self, head: Item = None):
        self.head = head
        self.count = 0 if head is None else 1

    def append_item(self, itm):
        item = Item(itm)
        if self.head is None:
            self.head = item
        else:
            curr_item = self.head
            prev_item = None
            while curr_item:
                prev_item = curr_item
                curr_item = curr_item.next_item
            prev_item.next_item = item
        self.count += 1

    def insert_at_position(self, data, position):
        if position > self.size():
            raise Exception(f'LinkedList length is {self.size()}, hence position doesn\'t exist. '
                            f'To append use index {self.size()}')

        if position < 0:
            raise Exception('Position cannot be negative')

        new_item = Item(data)
        if position == 0:
            self.insert_at_the_beginning(new_item)
            self.count += 1
            return

        curr_index = 0
        curr_item: Item = self.head
        while curr_index + 1 < position:
            curr_item = curr_item.next_item
            curr_index += 1
        tmp: Item = curr_item.next_item
        curr_item.next_item = new_item
        new_item.next_item = tmp
        self.count += 1
        return self.head

    def insert_at_the_beginning(self, item):
        curr_head = self.head
        self.head = item
        self.head.next_item = curr_head
        self.count += 1
        return self.head

    def size(self):
        return self.count

    def get_at_position(self, position):
        if position > self.size() - 1:
            raise Exception(f'LinkedList length is {self.size()}, hence position {position} doesn\'t exist.')

        if position < 0:
            raise Exception('Position cannot be negative')

        curr_index = 0
        curr_item = self.head

        while curr_index < position:
            curr_item = curr_item.next_item
            curr_index += 1
        return curr_item.value

    def remove_at_position(self, position):
        if position > self.size() - 1:
            raise Exception(f'LinkedList length is {self.size()}, hence position {position} doesn\'t exist.')

        if position < 0:
            raise Exception('Position cannot be negative')

        if position == 0:
            self.remove_at_the_beginning()

        curr_index = 0
        curr_item = self.head
        while curr_index + 1 < position:
            curr_item = curr_item.next_item
            curr_index += 1
        item_to_remove: Item = curr_item.next_item
        curr_item.next_item = item_to_remove.next_item
        self.count -= 1
        return item_to_remove.value

    def remove_at_the_beginning(self):
        curr_head = self.head
        next_item = curr_head.next_item
        self.head = next_item
        self.count -= 1
        return curr_head.value

    def print_linked_list(self):
        print()
        temp: Item = self.head
        while temp:
            print(temp.value, ', ', end='')
            temp: Item = temp.next_item
        print()


def convert_arraylist_to_linked_list(array_list: list):
    linked_list = LinkedList()
    for item in array_list:
        linked_list.append_item(item)
    return linked_list
