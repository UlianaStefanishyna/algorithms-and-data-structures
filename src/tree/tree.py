class Tree:
    """abstract class for Tree DS"""

# --------------------------------nested Position class--------------------------------
    class Position:
        """abstraction for a location of a single element"""

        def element(self):
            """:returns element stored at this position"""
            raise NotImplementedError()

        def __eq__(self, other) -> bool:
            """:returns True if other Position represents the same location"""
            raise NotImplementedError()

        def __ne__(self, other) -> bool:
            """:returns True if other doesn't represent the same location."""
            return not (self == other)

    # --------------------------------abstract methods that concrete subclass must support---------------------
    def root(self):
        """:returns Position representing the Tree's root. (or None if empty)"""
        raise NotImplementedError()

    def parent(self, p: Position):
        """:returns Position representing the p's parent. (or None if p is root)"""
        raise NotImplementedError()

    def num_children(self, p: Position) -> int:
        """:returns the number of children that Position p has."""
        raise NotImplementedError()

    def children(self, p: Position):
        """generates an iteration of Positions representing p's children"""
        raise NotImplementedError()

    def __len__(self) -> int:
        """:returns the total number of elements in the Tree. Usafe `len(T)`"""
        raise NotImplementedError()

    # --------------------------------concrete methods implemented in this class---------------------
    def is_root(self, p: Position) -> bool:
        """:returns True if Position p represents the root of the Tree."""
        return self.root() == p

    def is_leaf(self, p: Position) -> bool:
        """:returns True is Position p does not have any children"""
        return self.num_children(p) == 0

    def is_empty(self) -> bool:
        """:returns True if the Tree is empty"""
        return len(self) == 0

    def depth(self, p: Position) -> int:  # O(n) worst case
        """:returns the number of leaves separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height(self, p: Position = None) -> int:  # O(n) worst case
        """:returns height of a subtree with the rooted at Position p"""
        # top-down fashion
        if p is None:
            p = self.root()
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height(c) for c in self.children(p))

    def __iter__(self):
        """Generates an iteration of the tree's elements. Usafe `iter(T)`"""
        for p in self.positions():
            yield p.element()

    def positions(self):
        """Generates an iteration of all positions of tree T"""
        raise self.preorder()

    def preorder(self):
        """Generates a preorder iterations in the tree.
        Is a generator function which yields all the positions to the caller.
        The caller could then use a for loop to get each yielded position: `for p in T.preorder():<"visit" position p>`
        """
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def postorder(self):
        """Generates a postorder iterations in the tree.
        Is a generator function which yields all the positions to the caller.
        The caller could then use a for loop to get each yielded position: `for p in T.preorder():<"visit" position p>`
        """
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """Generates a preorder iteration of positions in subtree rooted at p."""
        yield p                                      # visit p before its subtrees
        for c in self.children(p):
            for other in self._subtree_preorder(c):  # do preorder of c's subtree
                yield other                          # yielding each to our caller

    def _subtree_postorder(self, p):
        """Generates a postorder iteration of positions in subtree rooted at p."""
        for c in self.children(p):
            for other in self._subtree_postorder(c):  # do postorder of c's subtree
                yield other                           # yielding each to our caller
        yield p                                       # visit p after its subtrees


""" 
Tree representation using intent (1), label (2), and parenthesis (3)
"""


def preorder_intent(T: Tree, p: Tree.Position, d: int):
    """Print preorder representation of T rooted at p at depth d."""
    print(2*d*' ' + str(p.element()))    # use depth for indentation
    for c in T.children(p):
        preorder_intent(T, c, d + 1)


def preorder_label(T: Tree, p: Tree.Position, d: int, path: list):
    """Print labeled representation of subtree of T rooteed at p at depth d."""
    label = '.'.join(str(j+1) for j in path)
    print(2*d*' ' + label, p.element())
    path.append(0)
    for c in T.children(p):
        preorder_label(T, c, d+1, path)
        path[-1] += 1
    path.pop()


def parenthesize(T: Tree, p: Tree.Position):
    """Prints parenthesized representation of subtree of T rooted at p."""
    print(p.element(), end='')
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = ' (' if first_time else ', '
            print(sep, end='')
            first_time = False
            parenthesize(T, c)
        print(')', end='')
