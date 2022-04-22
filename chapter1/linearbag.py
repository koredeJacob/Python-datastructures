class Bag:
    def __init__(self):
        self._theitems=[]
    def __len__(self):
        return len(self._theitems)
    def __contains__(self,item):
        return item in self._theitems
    def add(self,item):
        return self._theitems.append(item)
    def remove(self,item):
        assert item in self._theitems,"the  items mut be in the bag"
    def __iter__(self):
        return _BagIterator(self._theitems)

class _BagIterator:
    def __init__(self,theList):
        self._bagItems=theList
        self._curItem=0

    def __iter__(self):
        return self
    def __next__(self):
        if self._curItem<len(self._bagItems):
            item=self._bagItems[self._curItem]
            self._curItem+=1
            return item
        else:
            raise StopIteration

x=Bag()
x.add(7)
print ((7 in x))