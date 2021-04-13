from empty import Empty

class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if(self.is_empty()):
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if(self.is_empty()):
            raise Empty('Stack is empty')
        return self._data.pop()


def is_matched(expr):
    lefty = '({['
    righty = ')}]'

    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()


def main():
    S = ArrayStack()
    S.push(5)
    S.push(3)
    print(len(S))
    print(S.pop())
    print(S.is_empty())
    print(S.pop())
    print(S.is_empty())
    S.push(7)
    S.push(9)
    print(S.top())
    S.push(4)
    print(len(S))

    print(is_matched('()(())'))
    print(is_matched('()({(}))'))


# stack are used for browser recent searches and undo in text
# another use case is to reverse a set of texts, lines or numbers
if __name__ == "__main__":
    main()
