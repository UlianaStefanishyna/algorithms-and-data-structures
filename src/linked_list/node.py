class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data
