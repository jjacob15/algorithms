import math


class SimpleBinaryTree:
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class _PrintNode:
        __slots__ = '_node', '_level'

        def __init__(self, node, level=0):
            self._node = node
            self._level = level

    def __init__(self):
        self._root = None

    def root(self):
        if self._root is None:
            return None
        return self._root

    def parent(self, node):
        if node._parent is None:
            return None
        return node._parent

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

    def print(self):
        print()
        print('-----printing structure-----')
        queue = []
        queue.append(self._PrintNode(self.root()))
        currentLevel = 0
        print('0 -> ',  end="", flush=True)
        while len(queue) != 0:
            printNode = queue.pop(0)
            node = printNode._node
            if(currentLevel != printNode._level):
                print()
                print(str(printNode._level) + ' -> ',  end="", flush=True)
            print(str(node._element) + ('(' + str(node._parent._element) +
                  ')' if node._parent is not None else '') + ' ',  end="", flush=True)
            currentLevel = printNode._level

            if self.left(node):
                queue.append(self._PrintNode(
                    self.left(node), printNode._level+1))
            if self.right(node):
                queue.append(self._PrintNode(
                    self.right(node), printNode._level+1))
    
    # ------------------- tree restructure / trinode restructure------------------
    def _relink(self, parent, child, make_left_child):
        if make_left_child:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child._parent = parent


    def _rotate(self,p):
        print()
        x = p
        y = x._parent #assuming it exists
        z = y._parent #grandparent
        
        if z is None:
            self._root = x
            x._parent = None
        else:
            self._relink(z, x, z._left == y)

        if x == y._left:
            self._relink(y, x._right, True)
            self._relink(x, y, False)
        else:
            self._relink(y, x._left, False)
            self._relink(x, y, True)



    def _restructure(self, x):
        y = self.parent(x)
        z = self.parent(y)
        if( z is None):
            return
        if((x == self.right(y)) == (y == self.right(z)) or ((x == self.left(y)) == (y == self.left(z)))):
            print('rotating onces')
            self._rotate(y)
        else:
            print('rotating twice')
            self._rotate(x)
            self._rotate(x)
    # ----------------------------------------------------------------------------

    def _add(self, v, p):
        if p is None:
            self.add_root(v)
        elif v < p._element:
            if(self.left(p) is None):
                self.add_left(v, p)
            else:
                self._add(v, self.left(p))
        else:  # value is greater than node,adding to the right
            if(self.right(p) is None):
                self.add_right(v, p)
            else:
                self._add(v, self.right(p))

    def add(self,v):
        if(self._root is None):
            self._add(v, None)
        else:
            self._add(v, self.root())

class TestForTriNodeRestructure:
    def __init__(self):
        self._tree = SimpleBinaryTree()
    def run(self):
        root = self._tree.add_root(10)
        six = self._tree.add_left(6, root)
        twelve = self._tree.add_right(12, root)
        four =self._tree.add_left(4,six)
        self._tree.add_right(7, six)
        two =self._tree.add_left(2,four)
        self._tree.add_right(5, four)

        self._tree.print()
        self._tree._restructure(four)
        self._tree.print()


class TestForAddition:
    def __init__(self):
        self._tree = SimpleBinaryTree()
    def run(self):
        self._tree.add(10)
        self._tree.add(6)
        self._tree.add(12)
        self._tree.add(4)
        self._tree.add(7)
        self._tree.add(2)
        self._tree.add(5)
        self._tree.add(5)
        self._tree.print()


if __name__ == "__main__":
    tree = SimpleBinaryTree()
    # #------------------- Test for trinode rotation -------------------
    # T = TestForTriNodeRestructure()
    # T.run()
    # #------------------------------------------------------------
    T = TestForAddition()
    T.run()
    # ----------------------- Test for addition ----------------------- 

