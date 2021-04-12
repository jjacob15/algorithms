import ctypes

class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
    
    def _make_array(self,c):
        return (c * ctypes.py_object)()


d = DynamicArray()
d._make_array(10)        