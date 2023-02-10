from src.tree.binary_tree import BinaryTree
from src.tree.tree import preorder_label, preorder_intent, parenthesize


class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p: Position):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node: _Node) -> Position:
        """:returns Position instance for a given node"""
        return self.Position(self, node) if node is not None else None

    # ------ binary tree constructor ------
    def __init__(self):
        self._root = None
        self._size = 0

    # ------ public accessors ------
    def __len__(self):  # O(1) time
        return self._size

    def root(self):  # O(1) time
        return self._make_position(self._root)

    def parent(self, p):  # O(1) time
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):  # O(1) time
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):  # O(1) time
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p: Position) -> int:  # O(1) time
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    # ------ private update methods ------

    def _add_root(self, e) -> Position:  # O(1) time
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e) -> Position:  # O(1) time
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e) -> Position:  # O(1) time
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):  # O(1) time
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):  # O(1) time
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children, cannot be deleted')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):  # O(1) time
        node = self._validate(p)
        if not self.is_leaf(p):  # O(1) time
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():  # O(1) time
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2.size = 0

    def insert(self, root: Position, node):
        if root is None:
            self._add_root(node)
        else:
            if root < node:
                if root.right is None:
                    root.right = node
                else:
                    insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    insert(root.left, node)


def _insert_into_binary_tree(tree: LinkedBinaryTree, element: int, position: LinkedBinaryTree.Position = None,
                             is_left: bool = False, is_right: bool = False) -> LinkedBinaryTree.Position:
    if not is_left and not is_right:
        return tree._add_root(element)
    elif is_left and not is_right:
        return tree._add_left(position, element)
    elif is_right:
        return tree._add_right(position, element)


def preorder_label_1(position: LinkedBinaryTree.Position, label):
    position._node.label = label
    if position._node._left:
        preorder_label_1(position._node._left, 2 * label)
    if position._node._right:
        preorder_label_1(position._node._right, 2 * label + 1)


if __name__ == '__main__':
    # data = [10, 5, 15, 3, 7, 13, 17]
    data = [5, 3, 7, 2, 4, 6, 8]
    # data = ['/', '*', '+', '+', '4', '-', '2', '3', '1', '', '', '9', '5', '', '']
    binary_tree = LinkedBinaryTree()

    root = binary_tree._add_root(data[0])
    current_position = root

    for i in range(1, len(data)):
        if i % 2 == 1:
            current_position = binary_tree._add_left(current_position, data[i])
        else:
            current_position = binary_tree._add_right(current_position, data[i])

    depth = binary_tree.depth(root)
    # preorder_label_1(root, 1)
    # preorder_intent(binary_tree, root, depth)
    parenthesize(binary_tree, root)

