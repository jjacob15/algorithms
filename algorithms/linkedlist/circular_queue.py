from ..common.empty import Empty


class CircularQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('The queue is empty')

        if self._size == 1:
            return self._tail._element
        else:
            return self._tail._next._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('The queue is empty')

        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next

        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        newElement = self._Node(e, None)

        if self.is_empty():
            newElement._next = newElement
        else:
            newElement._next = self._tail._next
            self._tail._next = newElement

        self._tail = newElement
        self._size += 1


def test():
    L = CircularQueue()
    print('adding BOS', L.enqueue('BOS'))
    print(L.first())
    print('adding ATL', L.enqueue('ATL'))
    print('adding MSP', L.enqueue('MSP'))
    print('adding LAX', L.enqueue('LAX'))
    print(len(L))
    print('Current first:', L.first())
    print(L.dequeue())
    print('Current new first:', L.first())


if __name__ == "__main__":
    test()