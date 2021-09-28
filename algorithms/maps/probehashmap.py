from hash.hashmapbase import HashMapBase

class ProbeHashMap(HashMapBase):
    _AVAIL  = object()

    def _is_available(self,j):
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL
    
    def _find_slot(self,j,k):
        """Search for key k in bucket at index j.
        Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location.
        If no match found, success is False and index denotes first available slot.
        """
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j
                if self._table[j] is None:
                    return (False, firstAvail)
            elif k == self._table[j]._key:
                return (True,j)
            j = (j +1) % len(self._table)

    def _bucket_getitem(self,j,k):
        found, s = self._find_slot(j,k)
        if not found:
            raise KeyError('Key error :' ,repr(k))
        return self._table[s]._value

    def _bucket_setitem(self,j,k,v):
        found, s = self._find_slot(j,k)
        if not found:
            self._table[s] = self._Item(k,v)
            self._n += 1
        else:
            self._table[s]._value = v

    def _bucket_delitem(self,j,k):
        found, s = self._find_slot(j,k)
        if not found:
             raise KeyError('Key eerror :' ,repr(k))
        self._table[s] = ProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key


if __name__ == '__main__':
    class Id():
        __slots__ = "_name", "_number"
        def __init__(self,name,number):
            self._name= name
            self._number = number

    M = ProbeHashMap()
    jaison = Id('jaison', '0413039523')
    tina = Id('tina', '0432818243')
    M[jaison] = 'my name is jaison'
    M[tina] = 'my name is teena'

    print(M[tina])
    print(M[jaison])
    M[tina] = 'I changed my name to Tina'
    print(M[tina])


    M2 = ProbeHashMap()
    
    for i in range(100):
        M2[i] = i
    print(len(M2))

    for i in range(100):
        del M2[i]
    
    print(len(M2))
