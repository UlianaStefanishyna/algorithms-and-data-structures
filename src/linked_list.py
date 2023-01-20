class SinglyLinkedListNode(object):
    def __init__(self, data: int):
        self.data = data
        self.next = None


class SinglyLinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0


def insertNodeAtPosition(llist: SinglyLinkedList, data: int, position: int):
    if llist is None:
        llist = SinglyLinkedList()







    node = SinglyLinkedList()
    node.data = data
    node.next = None

    if position == 0:
        node.next = llist
        return node

    if position == 1:
        llist.next = node
        return llist

    counter = 1
    current_node = llist.next
    previous_node = llist
    while current_node:
        if counter == position:
            previous_node.next = node
            node.next = current_node
        previous_node = current_node
        current_node = current_node.next
        counter += 1

    return llist
