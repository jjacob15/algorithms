from .priority_queue_base import PriorityQueueBase
from ..linkedlist.doublylinkedlist.positional_list import PositionalList
from ..common.empty import Empty


class UnsortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.add_last(self._item(key, value))

    def _find_min(self):
        """Return Position of item with minimum key"""
        if self.is_empty():
            raise Empty('Priority queue is empty')

        small = self._data.first()
        walk = self._data.after(small)

        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)

        return small

    def min(self):
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)

def test():
    Q = UnsortedPriorityQueue()
    Q.add(1, 'Jaison')
    Q.add(2, 'Tina')
    Q.add(4, 'Benson')
    Q.add(3, 'Ryan')

    print(len(Q))
    print(Q.min())
    print(Q.remove_min())
    print(Q.remove_min())
    print(Q.remove_min())
    print(Q.remove_min())

if __name__ == "__main__":
    test()
