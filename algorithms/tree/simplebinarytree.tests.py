from simplebinarytree import SimpleBinaryTree

class TestForTriNodeRestructure:
    def __init__(self):
        self._tree = SimpleBinaryTree()
    def run(self):
        root = self._tree.add_root(10)
        six = self._tree.add_left(6, root)
        twelve = self._tree.add_right(12, root)
        four =self._tree.add_left(4,six)
        self._tree.add_right(7, six)
        two =self._tree.add_left(2,four)
        self._tree.add_right(5, four)

        self._tree.print()
        self._tree._restructure(four)
        self._tree.print()


class TestForAddition:
    def __init__(self):
        self._tree = SimpleBinaryTree()
    def run(self):
        self._tree.add(10)
        self._tree.add(6)
        self._tree.add(12)
        self._tree.add(4)
        self._tree.add(7)
        self._tree.add(2)
        self._tree.add(5)
        self._tree.print()

class TestUnbalanced:
    def __init__(self):
        self._tree = SimpleBinaryTree()
    def run(self):
        self._tree.add(1)
        self._tree.add(2)
        self._tree.add(3)
        self._tree.add(4)
        self._tree.add(5)
        self._tree.add(6)
        self._tree.add(7)
        self._tree.print()

if __name__ == "__main__":
    tree = SimpleBinaryTree()
     # #------------------- Test for trinode rotation -------------------
    # T = TestForTriNodeRestructure()
    # T.run()
    # #------------------------------------------------------------
    # T = TestForAddition()
    # T.run()
    # ----------------------- Test for addition ----------------------- 
    T  = TestUnbalanced()
    T.run()