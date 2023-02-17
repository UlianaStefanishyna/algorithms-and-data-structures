class EulerTour:
    def __init__(self, tree):
        self._tree = tree

    def tree(self):
        return self._tree

    def execute(self):
        if len(self._tree) > 0:
            self._tour(self._tree.root(), 0, [])

    def _tour(self, p, d, path):
        self._hook_previsit(p. d. p, d, path)
        results = []
        path.append(0)
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path))
            path[-1] += 1
        path.pop()
        return self._hook_post_visit(p, d, path, results)

    def _hook_previsit(self, p, d, path):
        pass

    def _hook_post_visit(self, p, d, path, result):
        pass


