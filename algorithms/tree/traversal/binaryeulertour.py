from .eulertour import EulerTour


class BinaryEulerTour(EulerTour):
    def _tour(self, p, d, path):
        result = [None, None]
        self._hook_previsit(p, d, path)
        if self._tree.left(p) is not None:
            path.append(0)
            result[0] = self._tour(self._tree.left(p), d+1, path)
            path.pop()
        self._hook_invisit(p, d, path)
        if self._tree.right(p) is not None:
            path.append(1)
            result[1] = self._tour(self._tree.right(p), d+1, path)
            path.pop()
        answer = self._hook_postvisit(p, d, path, result)
        return answer

    def _hook_invisit(p, d, path):
        pass
