
class SimpleBinaryTree:
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    def __init__(self):
        self._root = None

    def root(self):
        if self._root is None:
            return None
        return self._root

    def left(self, node):
        if node._left is None:
            return None
        return node._left
    
    def right(self, node):
        if node._right is None:
            return None
        return node._right

    def add_root(self, elem):
        self._root = self._Node(elem)
        return self._root
    
    def add_left(self, elem, parent):
        parent._left = self._Node(elem, parent)
        return parent._left

    def add_right(self, elem, parent):
        parent._right = self._Node(elem, parent)
        return parent._right

    def preorder(self, node):
        if node:
            print(node._element, end="", flush=True)
            self.preorder(self.left(node))
            self.preorder(self.right(node))

    def inorder(self, node):
        if node:
            self.inorder(self.left(node))
            print(node._element, end="", flush=True)
            self.inorder(self.right(node))

    def postorder(self, node):
        if node:
            self.postorder(self.left(node))
            self.postorder(self.right(node))
            print(node._element, end="", flush=True)




if __name__ == "__main__":
    tree = SimpleBinaryTree()
    root = tree.add_root(1)
    two = tree.add_left(2, root)
    three = tree.add_right(3, root)
    tree.add_left(4,two)
    tree.add_right(5,two)

    print('Printing inorder')
    tree.inorder(root)
    print("")
    print('Printing preorder')
    tree.preorder(root)
    print("")
    print('Printing postorder')
    tree.postorder(root)
