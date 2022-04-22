import MapBase


class UnsortedTableMap(MapBase):
    def __init__(self):
        self._table = []

    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item.value
        raise KeyError("key error: "+repr(k))

    def __setitem__(self, k, v):
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):

        for i in range(len(self._table)):
            if k == self._table[i]._key:
                self._table.pop(i)
            return
        raise KeyError('keyError: '+repr(k))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item
