""" A heap is a min/max priority queue that ensures that its children are always less than or greater than it.
Adding values goes to the left and then right.
After the add, you do a swap with the parent until the added node priority is lesser than child node.
"""
from ..priority_queue_base import PriorityQueueBase


class HeapPriorityQueue(PriorityQueueBase):
    def _parent(self, j):
        return (j-1)//2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j+2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right

            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)
