class UnbalancedPriorityHeap:
    class _Item:
        __slots__ = "_key", "_value", "_left", "_right"

        def __init__(self, k, v, p=None):
            self._key = k
            self._value = v
            self._left = None
            self._right = None
            self._parent = p

        def __lt__(self, other):
            return self._key < other._key

    def __init__(self):
        self._root = None
        self._last = None

    def add(self, k, v):
        if not self._last:
            self._root = self._Item(k, v)
            self._last = self._root
        else:
            if self._last._left is None:
                self._last._left = self._Item(k, v,self._last)
            elif self._last._right is None:
                self._last._right = self._Item(k, v, self._last)
            else:
                first = self._last._left
                first._left = self._Item(k, v, self._last._left)
                self._last = first

    def print(self):
        self._preorder(self._root)

    def _preorder(self, e):
        print(e._key, e._value)
        if e._left:
            self._preorder(e._left)
        if e._right:
            self._preorder(e._right)

    def _swap(self,i,j):
        pass

    def _upheap(self):
        pass
    def _downheap(self):
        pass


if __name__ == "__main__":
    P = UnbalancedPriorityHeap()
    P.add(1, 'a')
    P.add(2, 'b')
    P.add(3, 'c')
    P.add(4, 'd')
    P.add(5, 'e')
    P.print()
