class LinkedList:
    class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next_node = next_node

    def __init__(self, head=None):
        self.head = head

    def put(self, value):
        curr_head = self.head
        new_node = self.Node(value)
        new_node.next_node = curr_head
        self.head = new_node

    def pop(self):
        curr_head = self.head
        value = self.head.value
        self.head = curr_head.next_node
        return value

    def generator(self):
        pointer = self.head
        while pointer:
            yield pointer.value
            pointer = pointer.next_node


def enqueue(s1, s2, value):
    s1.put(value)
    while s2.head:
        s2.pop()
    for i in s1.generator():
        s2.put(i)


def dequeue(s1, s2, **kwargs):
    el = s2.pop()
    while s1.head:
        s1.pop()
    for i in s2.generator():
        s1.put(i)
    return el


def print_q(s2, **kwargs):
    print(s2.head.value)


types = {
    '1': enqueue,
    '2': dequeue,
    '3': print_q
}


def func(q):

    stack1 = LinkedList()
    stack2 = LinkedList()
    for i in range(int(q)):
        type_num = input()
        if len(type_num.split(' ')) > 1:
            t = type_num.split(' ')[0]
            v = type_num.split(' ')[1]
        else:
            t = type_num
        f = types[t]
        f(s1=stack1, s2=stack2, value=v)


if __name__ == '__main__':
    q = input()
    func(q)
