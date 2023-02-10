from src.tree.tree import Tree
from typing import Optional


class BinaryTree(Tree):

    # --------------------------------additional abstract methods ---------------------
    def left(self, p: Tree.Position) -> Tree.Position:
        """:returns a Position representing p's left child"""
        raise NotImplementedError()

    def right(self, p: Tree.Position) -> Tree.Position:
        """:returns a Position representing p's right child"""
        raise NotImplementedError()

    # --------------------------------concrete methods implemented here---------------------
    def sibling(self, p: Tree.Position) -> Optional[Tree.Position]:
        """:returns a Position representing p's sibling (or None if no)"""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p: Tree.Position):
        """generates an iteration of Positions representing p's children"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def positions(self):
        return self.inorder()

    def num_children(self, p: Tree.Position) -> int:
        return len([child for child in self.children(p)])

    def _subtree_inorder(self, p):
        """Generates a inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p  # visit p in between its subtrees
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other
