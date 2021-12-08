import math


class SimpleBinaryTree:
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right', '_height'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
            self._height = 0

        def left_height(self):
            return self._left._height if self._left is not None else 0

        def right_height(self):
            return self._right._height if self._right is not None else 0

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
            self._rotate(y)
            return y
        else:
            self._rotate(x)
            self._rotate(x)
            return x
    # ----------------------------------------------------------------------------

    def _add(self, v, p):
        if p is None:
            self.add_root(v)
        elif v < p._element:
            if(self.left(p) is None):
                return self.add_left(v, p)
            else:
                return self._add(v, self.left(p))
        else:  # value is greater than node,adding to the right
            if(self.right(p) is None):
                return self.add_right(v, p)
            else:
                return self._add(v, self.right(p))

    def add(self,v):
        if(self._root is None):
            self._add(v, None)
        else:
            added = self._add(v, self.root())
            self._rebalance(added)

    def _recompute_height(self,p):
        p._height = 1 + \
            max(p.left_height(), p.right_height())

    def _isbalanced(self, p):
        return abs(p.left_height() - p.right_height()) <= 1
    
    def _tall_child(self, p, favorleft = False):
        if p.left_height() + ( 1 if favorleft else 0) > p.right_height():
            return self.left(p)
        else:
            return self.right(p)

    def _tall_grandchild(self,p):
        child = self._tall_child(p)
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)

    def _rebalance(self, p):
        while p is not None:
            old_height = p._height
            if not self._isbalanced(p):
                p = self._restructure(self._tall_grandchild(p))
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)
            if p._height == old_height:
                p = None
            else:
                p = self.parent(p)

