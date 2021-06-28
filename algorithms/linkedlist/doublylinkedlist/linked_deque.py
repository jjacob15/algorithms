from doublylinkedbase import _DoublyLinkedBase
from ...common.empty import Empty


class LinkedDeque(_DoublyLinkedBase):
    # Double-ended queue implementation based on a doubly linked list.

    def first(self):
        if self.is_empty():
            raise Empty('Deque is empty')

        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev._element

    def insert_first(self, e):
        self._insert_between(self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        self._delete_node(self._trailer._prev)
