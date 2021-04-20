from .binarytree import BinaryTree


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

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be a proper Position type')
        # remember the container is a reference to the LinkedBinaryTree.
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, node):
        return self._make_position(node._parent)

    def left(self, node):
        return self._make_position(node._left)

    def right(self, node):
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1

        return count

    def _add_root(self, e):
        if self._root is not None:
            raise ValueError('Tree is not empty')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p had two children')
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

    def _attach(self, p, t1, t2):
        raise NotImplementedError('will do later')


def _run_test():
    S = LinkedBinaryTree()
    print(S.root())
    root = S._add_root("Jacob")
    print(S.root()._node._element)
    jaison = S._add_left(root, 'Jaison')
    benson = S._add_right(root, 'Benson')
    tina = S._add_left(jaison, 'Tina')
    ryan = S._add_right(jaison, 'Ryan')

    print(S.num_children(root))
    print(S.num_children(jaison))
    print(S.num_children(benson))

    print(len(S))

    print(S.is_left(ryan))
    print(S.is_left(jaison))

    print(S._replace(benson, 'Bini'))

    print(type(ryan))
    print(S.depth(ryan._node))

if __name__ == '__main__':
    _run_test()
