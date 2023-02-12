
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # if self.root:
        #     self._insert_into_bst(self.root, new_val)
        # else:
        #     self.root = Node(new_val)
        self._insert_into_bst_concise(self.root, new_val)

    def _insert_into_bst(self, parent: Node, value: int):
        if value < parent.value:
            child = parent.left
        else:
            child = parent.right
        if child:
            self._insert_into_bst(child, value)
        else:
            if value < parent.value:
                parent.left = Node(value)
            else:
                parent.right = Node(value)

    def _insert_into_bst_concise(self, parent: Node, value: int) -> Node:
        if not parent:
            return Node(value)
        if value < parent.value:
            parent.left = self._insert_into_bst_concise(parent.left, value)
        else:
            parent.right = self._insert_into_bst_concise(parent.right, value)
        return parent

    def print(self):
        res = self.preorder_print(self.root, '')
        print(res)
        return res

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a recursive print solution."""
        if start is None:
            return traversal
        if start.value:
            if traversal != '': traversal += '-'
            traversal += str(start.value)
            traversal = self.preorder_print(start.left, traversal)
            return self.preorder_print(start.right, traversal)

    def search(self, find_val):
        return self._search_in_bst(self.root, find_val)

    def _search_in_bst(self, parent: Node, value: int) -> bool:
        if not parent:
            return False
        if parent.value == value:
            return True

        if value < parent.value:
            child = parent.left
        else:
            child = parent.right
        return self._search_in_bst(child, value)


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