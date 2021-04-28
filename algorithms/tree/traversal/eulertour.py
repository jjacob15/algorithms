class EulerTour:
    # _hook_previsit and_hook_postvisit may be overridden by subclasses
    def __init__(self, tree):
        self._tree = tree

    def tree(self):
        return self._tree

    def execute(self):
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])

    def _tour(self, p, d, path):
        """
        p       Position of current node being visited
        d       depth of p in the tree
        path    list of indices of children on path from root to p
        """
        self._hook_previsit(p, d, path)
        result = []
        path.append(0)
        for c in self._tree.children(p):
            result.append(self._tour(c, d+1, path))
            path[-1] += 1
        path.pop()
        answer = self._hook_postvisit(p, d, path, result)
        return answer

    def _hook_previsit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d, path, result):
        pass
