"""
Coursera course Algorithms Part I by Princetone University
@link: https://www.coursera.org/learn/algorithms-part1 (week1)
"""
class UnionFind:

    def __init__(self, length: int, array=None):
        if not array:
            self.array = [i for i in range(length)]
        else:
            self.array = array
        self.tree_size_of = [0] * length

    def connected(self, p, q) -> bool:
        return self.array[p] == self.array[q]

    def union(self, p, q): # always unique as they're indices
        id_p = self.array[p] # get actually a connectivity value of this index
        id_q = self.array[q]
        for i in range(len(self.array)):
            if self.array[i] == id_p:
                self.array[i] = id_q # change all p-connected values to the q-index
        return self.array

    # Based on the Tree Forest DS where each connected item points to its root
    def quick_union(self, p, q):
        root_p = self._root_of(p)
        root_q = self._root_of(q)
        self.array[root_p] = root_q
        return self.array

    def quick_union_weighted(self, p, q, path_comression=False):
        root_p = self._root_of(p, path_comression)
        root_q = self._root_of(q)
        if root_p == root_q:
            return
        if self.tree_size_of[root_p] < self.tree_size_of[root_q]:
            self.array[root_p] = root_q
            self.tree_size_of[root_q] += self.tree_size_of[root_p]
        else:
            self.array[root_q] = root_p
            self.tree_size_of[root_p] += self.tree_size_of[root_q]

    def connected_quick_union(self, p, q):
        return self._root_of(p) == self._root_of(q)

    def _root_of(self, index, path_comression=False):
        while index != self.array[index]:
            if path_comression:
                self.array[index] = self.array[self.array[index]]
            index = self.array[index]
        return index

    def print(self):
        print(self.array)


if __name__ == '__main__':
    uf = UnionFind(10, [0, 1, 1, 8, 8, 0, 0, 1, 8, 8])
    assert uf.union(6, 1) == [1, 1, 1, 8, 8, 1, 1, 1, 8, 8]
    assert uf.connected(6, 1)

    uf_quick = UnionFind(10, [0, 1, 9, 4, 9, 6, 6, 7, 8, 9])
    assert uf_quick.quick_union(3, 5) == [0, 1, 9, 4, 9, 6, 6, 7, 8, 6]
    assert uf_quick.connected_quick_union(3, 5)

    uf_weighted = UnionFind(10, [0, 1, 9, 4, 9, 6, 6, 7, 8, 9])
    res_tree = uf_weighted.quick_union_weighted(3, 5)
    assert res_tree == [0, 1, 9, 4, 9, 6, 9, 7, 8, 9]
    assert uf_quick.connected_quick_union(3, 5)

    uf_weighted_path_compression = UnionFind(10, [0, 1, 9, 4, 9, 6, 6, 7, 8, 9])
    res_tree = uf_weighted.quick_union_weighted(3, 5, path_comression=True)
    assert res_tree == [0, 1, 9, 9, 9, 6, 9, 7, 8, 9]
    assert uf_quick.connected_quick_union(3, 5)
