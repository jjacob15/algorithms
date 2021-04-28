class Tree:
    class Position:
        def element(self):
            raise NotImplementedError('must be implmented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implmented by subclass')

        def __ne__(self, other):
            return not (self == other)

    def root(self):
        raise NotImplementedError('must be implmented by subclass')

    def parent(self, p):
        raise NotImplementedError('must be implmented by subclass')

    def num_children(self, p):
        raise NotImplementedError('must be implmented by subclass')

    def children(self, p):
        raise NotImplementedError('must be implmented by subclass')

    def __len__(self):
        raise NotImplementedError('must be implmented by subclass')

    def is_root(self, p):
        return self.root() == p

    def is_left(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):  # number of levels from p to root
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def positions(self):
        return self.preorder()

    def preorder(self):
        # generate a preorder iteration of positions in the tree
        if not self.is_empty():
            for p in self._subtree_preoder(self.root()):
                yield p

    def _subtree_preoder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preoder(c):
                yield other

    def postorder(self):
        # generate a postorder iteration of positions in the tree
        if not self.is_empty():
            for p in self._subtree_preoder(self.root()):
                yield p

    def _subtree_preoder(self, p):
        for c in self.children(p):
            for other in self._subtree_preoder(c):
                yield other
        yield p
