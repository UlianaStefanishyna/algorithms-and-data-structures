class Item:

    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def get_value(self):
        return self.value
