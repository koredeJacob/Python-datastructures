import ctypes

class Array:
    def __init__(self,size):
        assert size>0,"array size must be greater than zero"
        self._size=size
        pyArrayType=ctypes.py_object *size
        self._elements=pyArrayType()

        self._clear(None)
    def __len__(self):
        return self._size
    def __getitem__(self,index):
        assert index>=0 and index<len(self),"array subscript out of range"
        return self._elements[index]

    def clear(self,value):
        for i in range(len(self)):
            self._elements[i]=value
    def __setitem__(self,index,value):
        assert index>=0 and index<len(self),"array subscript out of range"
        self._elements[index]=value

    def __iter__(self):
        return _ArrayIterator(self._elements)

class _ArrayIterator:
    def __init__(self,thearray):
        self._arrayRef=thearray
        self._curNdx=0
    def __iter__(self):
        return self
    def __next__(self):
        if self._curNdx<len(self._arrayRef):
            entry=self._arrayRef[self._curNdx]
            self._curNdx+=1
            return entry
        else:
            raise StopIteration
class Array2D:
    def __init__(self,numRows,numCols):
        self._theRows=Array(numRows)

        for i in range(numRows):
            self._theRows[i]=Array(numCols)

    def numRows(self):
        return len(self._theRows)

    def numCols(self):
        return len(self._theRows[0])

    def clear(self,value):
        for row in range(self.numRows()):
            row.clear(value)

    def __getitem__(self,ndxTuple):
        assert len(ndxTuple)==2,"invalid number of array subscript"
        row=ndxTuple[0]
        col=ndxTuple[1]

        assert row>=0 and row<self.numRows()\
            and col>=0 and col<self.numCola(),"array subscript out of range"
        theidarray=self.theRows[row]
        theidarray[col]=value

         

