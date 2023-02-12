
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
        self._insert_into_bst(self.root, new_val)

    def _insert_into_bst(self, parent: Node, value: int):
        """helper for recursion to insert into BST"""
        # if parent is None:
        new_node = Node(value)
        if value < parent.value:
            child = parent.left
            if child is None:
                parent.left = new_node
                return
        else:
            child = parent.right
            if child is None:
                parent.right = new_node
                return
        self._insert_into_bst(child, value)

    def print(self):
        return self.preorder_print(self.root, '')

    def preorder_print(self, start: Node, traversal):
        """Helper method - use this to create a recursive print solution."""
        if start is None:
            return traversal
        if traversal != '':
            traversal += '-'
        traversal += str(start.value)
        traversal = self.preorder_print(start.left, traversal)
        return self.preorder_print(start.right, traversal)

    def search(self, find_val):
        """Public search method in BST"""
        return self._search_in_bst(self.root, find_val)

    def _search_in_bst(self, parent: Node, value: int) -> bool:
        """helper func or search recursion in BST"""
        if value == parent.value:
            return True
        if value < parent.value:
            child = parent.left
        else:
            child = parent.right
        if not child:
            return False
        return self._search_in_bst(child, value)


if __name__ == '__main__':
    # Set up tree
    tree = BST(4)

    # Insert elements
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)

    #      4
    #    2   5
    #  1  3

    assert tree.print() == '4-2-1-3-5'
    assert tree.search(4)
    assert not tree.search(10)
    assert not tree.search(6)