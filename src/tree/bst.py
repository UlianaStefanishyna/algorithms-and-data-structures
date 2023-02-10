
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        """Public method to insert into BST"""
        pass

    def _insert_into_bst(self, parent: Node, value: int):
        """helper for recursion to insert into BST"""
        pass

    def print(self):
        pass

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a recursive print solution."""
        pass

    def search(self, find_val):
        """Public search method in BST"""
        pass

    def _search_in_bst(self, parent: Node, value: int) -> bool:
        """helper func or search resursion in BST"""
        pass


if __name__ == '__main__':
    # Set up tree
    tree = BST(4)

    # Insert elements
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)

    assert tree.print() == '4-2-1-3-5'
    assert tree.search(4)
    assert not tree.search(10)
    assert not tree.search(6)