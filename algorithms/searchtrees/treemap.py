from ..tree.linkedbinarytree import LinkedBinaryTree
from ..maps.hash.mapbase import MapBase


class TreeMap(LinkedBinaryTree,MapBase):

    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self.element()._key
        def value(self):
            return self.element()._value

    def _subtree_search(self,p,k):
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
        