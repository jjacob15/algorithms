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

    def is_empty(self, p):
        return len(self) == 0

    def depth(self, p):  # number of levels from p to root
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
