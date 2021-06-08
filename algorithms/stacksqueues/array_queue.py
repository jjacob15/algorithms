from ..common.empty import Empty


class ArrayQueue:
    DEFAULT_CAPACITY = 11

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0  # number of elements in the queue
        self._front = 0  # the first element index

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        # needed to wrap around the queue
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None]*cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk) % len(old)
        self._font = 0


if __name__ == "__main__":
    Q = ArrayQueue()
    Q.enqueue(5)
    Q.enqueue(3)
    print(len(Q))
    print(Q.dequeue())
    print(Q.is_empty())
    print(Q.dequeue())
