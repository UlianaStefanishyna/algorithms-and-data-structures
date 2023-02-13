class Queue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def print_head(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        print(self.out_stack[-1])
        return self.out_stack[-1]


if __name__ == '__main__':
    q = input()
    queue = Queue()
    for i in range(int(q)):
        type_num = input()
        if len(type_num.split(' ')) > 1:
            t = type_num.split(' ')[0]
            v = type_num.split(' ')[1]
        else:
            t = type_num
        if t == '1':
            queue.enqueue(v)
        elif t == '2':
            queue.dequeue()
        else:
            queue.print_head()
