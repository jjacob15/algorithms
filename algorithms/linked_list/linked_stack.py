# linked list avoid the disadvantages of array based structures because
# 1 the length of dynamic array might be longer than the actual number of elements
# 2 amortized bounds of operation may be unacceptable in rea-time systems
# 3 insertion and deletion at interior positions are expensive

# linked list disadvantages are 1, cannot be efficiently accessed by index or tell what is the order of the element.
# 2 cannot remove tail object unless its a doubly linked list

from ..common.empty import Empty


class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


def test():
    L = LinkedStack()
    print('adding BOS',L.push('BOS'))
    print('adding ATL',L.push('ATL'))
    print('adding MSP',L.push('MSP'))
    print('adding LAX',L.push('LAX'))
    print(len(L))
    print('Current top:', L.top())
    print(L.pop())
    print('Current new top:', L.top())


if __name__ == "__main__":
    test()
