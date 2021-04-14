from ..common.empty import Empty


class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        newest = self._Node(e, None)  # would be the tail
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest

        self._tail = newest
        self._size += 1

    def first(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1

        if self.is_empty():
            self._tail = None
        return answer


def test():
    L = LinkedQueue()
    print('adding BOS', L.enqueue('BOS'))
    print('adding ATL', L.enqueue('ATL'))
    print('adding MSP', L.enqueue('MSP'))
    print('adding LAX', L.enqueue('LAX'))
    print(len(L))
    print('Current first:', L.first())
    print(L.dequeue())
    print('Current new first:', L.first())


if __name__ == "__main__":
    test()
