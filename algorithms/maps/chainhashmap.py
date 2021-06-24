from hash.hashmapbase import HashMapBase
from hash.unsortedtablemap import UnsortedTableMap


class ChainHashMap(HashMapBase):
    def _bucket_getitem(self,j,k):
        bucket = self._table[j]
        if bucket is None:
             raise KeyError('Key error:', repr(k))
        return bucket[k]

    def _bucket_setitem(self,j,k,v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        oldsize = len(self._table[j])
        self._table[j][k]= v
        if len(self._table[j]) > oldsize:
            self._n += 1

    def _bucket_delitem(self,j,k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('key error',repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key


if __name__ == '__main__':
    class Id():
        __slots__ = "_name", "_number"
        def __init__(self,name,number):
            self._name= name
            self._number = number

    M = ChainHashMap()
    jaison = Id('jaison', '0413039523')
    tina = Id('tina', '0432818243')
    M[jaison] = 'my name is jaison'
    M[tina] = 'my name is teena'

    print(M[tina])
    print(M[jaison])
    M[tina] = 'I changed my name to Tina'
    print(M[tina])


    M2 = ChainHashMap()
    
    for i in range(100):
        M2[i] = i
    print(len(M2))

    for i in range(100):
        del M2[i]
    
    print(len(M2))