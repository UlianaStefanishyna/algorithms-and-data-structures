class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree: # Binary Tree, not a BST
    def __init__(self, root):
        self.root = Node(root)

    def search(self, final_val):
        """Return True if the value is in the tree, return False otherwise."""
        return self.preorder_search(self.root, final_val)

    def print_tree(self):
        """Print out all tree nodes as they are visited in a pre-order traversal."""
        return self.preorder_print(self.root, '')

    def preorder_search(self, start: Node, find_val: int):
        """Helper method - use this to create a recursive search solution."""
        if start is None:
            return False
        if find_val == start.value:
            return True
        return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a recursive print solution."""
        if start is None:
            return traversal
        if traversal != '':
            traversal += '-'
        traversal += str(start.value)
        traversal = self.preorder_print(start.left, traversal)
        return self.preorder_print(start.right, traversal)


if __name__ == '__main__':
    # Set up tree
    #      1
    #   2     3
    # 4  5  6  7
    tree_root_node = BinaryTree(1)
    tree_root_node.root.left = Node(2)
    tree_root_node.root.right = Node(3)
    tree_root_node.root.left.left = Node(4)
    tree_root_node.root.left.right = Node(5)
    tree_root_node.root.right.left = Node(6)
    tree_root_node.root.right.right = Node(7)

    assert tree_root_node.search(4)
    assert tree_root_node.search(6)
    assert not tree_root_node.search(8)
    assert tree_root_node.print_tree() == '1-2-4-5-3-6-7'
