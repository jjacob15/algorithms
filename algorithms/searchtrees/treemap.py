"""
Principals
- Left sub tree only contains values that are less than or equal to the nodes value
- Right sub tree only contains values that are greater than or equal to the nodes value
- Both left and right subtrees of all nodes are also binary search trees

Finding minimum, go down the left
Conversely, finding the maximum, go down the right

Finding a number, check the value of each node and go left or right depending on whether the nodes value is less than or greater than 
the one we are looking for

Printing all numbers, we could use inorder traversal, printing everything out in the left subtree, followed by printing the node itself and then follwed 
by printing everything out in the right subtree

Adding to the tree is relatively painless, follow the three principals of BST

Deleting is a bit more complicated.
- If the element is a leaf node, delete it
- Has only one child, delete the node an replace the child parent with the nodes parent
- Has two children, in this case, we need to find the node with the next largest value, swap them, and then delete the node in question. The node that
that has the next largest value can't have 2 children itself since its left child would be a better candidate for the next largest.

Disadvantages - if we were to make a tree from a sorted list, we would get an unbalanced skewed tree with all nodes to the right.
"""
from ..tree.linkedbinarytree import LinkedBinaryTree
from ..maps.hash.mapbase import MapBase


class TreeMap(LinkedBinaryTree,MapBase):

    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self.element()._key
        def value(self):
            return self.element()._value

    def _subtree_search(self, p, k):
        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p),k)
            else:
                if self.right(p) is not None:
                    return self._subtree_search(self.right(p),k)
            return p

    def _subtree_first_position(self,p):
        """Return position of first item at the left end"""
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk) 
        return walk
    def _subtree_last_position(self,p):
        """Return position of last item at the right end"""
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk) 
        return walk

    def first(self):
        """Return the position containing the least key, or None if the tree is empty"""
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def after(self,p):
        """Return the position containing the least key that is greater than that of
        position p (i.e., the position that would be visited immediately after p
        in an inorder traversal), or None if p is the last position.
        www.it-"""
        self._validate(p)
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above

    def before(self,p):
        """Return the position containing the greatest key that is less than that of
        position p (i.e., the position that would be visited immediately before p
        in an inorder traversal), or None if p is the first position"""
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def find_position(self, k):
        """Return position with key k, or else neighbor (or None if empty)."""
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p) # hook for balanced tree subclasses
            return p

    def find_min(self):
        """Return (key,value) pair with minimum key (or None if empty)."""
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())

    def find_ge(self, k):
        """Return (key,value) pair with least key greater than or equal to k.
        Return None if there does not exist such a key.
        """
        if self.is_empty():
            return None
        else:
            p = self.find_position(k) # may not find exact match
            if p.key() < k: # p’s key is too small
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None        

    def find_range(self, start, stop):
        """Iterate all (key,value) pairs such that start <= key < stop.
        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        """
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                # we initialize p with logic similar to find_ge
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)            

    def _relink(self, parent, child, make_left_child):
        """Relink parent node with child node. Child can be None"""
        if make_left_child:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child._parent = parent

    def _rotate(self,p):
        """Rotate Position p above its parent.
        Switches between these configurations, depending on whether p==a or p==b.
              b                  a
             / \                /  \
            a  t2             t0   b
           / \                     / \
          t0  t1                  t1  t2
        Caller should ensure that p is not the root.
        """        
        """Rotate Position p above it parent"""
        x = p._node
        y = x._parent #assuming it exists
        z = y._parent #grandparent

        if z is None:
            self._root = x # x becomes root
            x._parent = None
        else:
            self._relink(z, x, y == z._left) # x becomes a direct child of z

        # now rotate x and y, including transfer of middle subtree
        if x == y._left:
            self._relink(y, x._right, True) # x. right becomes left child of y
            self._relink(x,y,False) # y becomes right child of x
        else:
            self._relink(y,x._left,False)  # x. left becomes right child of y
            self._relink(x,y,True)  # y becomes left child of x

    def _restructure(self,x):
        """Perform a trinode restructure among Position x, its parent, and its grandparent.
        Return the Position that becomes root of the restructured subtree.
        Assumes the nodes are in one of the following configurations:
            z=a                 z=c           z=a               z=c
           /  \                /  \          /  \              /  \
          t0  y=b             y=b  t3       t0   y=c          y=a  t3
             /  \            /  \               /  \         /  \
            t1  x=c         x=a  t2            x=b  t3      t0   x=b
               /  \        /  \               /  \              /  \
              t2  t3      t0  t1             t1  t2            t1  t2
        The subtree will be restructured so that the node with key b becomes its root.
                  b
                /   \
              a       c
             / \     / \
            t0  t1  t2  t3
        Caller should ensure that x has a grandparent.
        """        
        """Perform trinode restructure of Position x with parent/grantparent"""
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y) == (y == self.right(z))): # matching alignment
            self._rotate(y)
            return y
        else:
            self._rotate(x)
            self._rotate(x)
            return x
        

    
    # ------------- public methods for (standard) map interface -------------
    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)  # hook for balanced tree subclasses
            if k != p.key():
                raise KeyError('Key Error: ' + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))  # from LinkedBinaryTree
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v  # replace existing item's value
                self._rebalance_access(p)  # hook for balanced tree subclasses
                return
            else:
                item = self._Item(k, v)
                if p.key() < k:
                    leaf = self._add_right(p, item)  # inherited from LinkedBinaryTree
                else:
                    leaf = self._add_left(p, item)  # inherited from LinkedBinaryTree
        self._rebalance_insert(leaf)  # hook for balanced tree subclasses

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)  # rely on positional version
                return  # successful deletion complete
            self._rebalance_access(p)  # hook for balanced tree subclasses
        raise KeyError('Key Error: ' + repr(k))

    def __iter__(self):
        """Generate an iteration of all keys in the map in order."""
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)


"""
          44                                
        /     \  
       /       \
      /         \
    17          88
   /  \       /    \
  8   32     65     97
      /     /  \   /
     28    54  82 93
      \       /
       29    76
              \
               80    
"""

"""
adding a node
          44                                
        /     \  
       /       \
      /         \
    17          88
   /  \       /    \
  8   32     65     97
      /     /  \   /
     28    54  82 93
      \       /
       29    76
            /  \
           68   80    
"""
