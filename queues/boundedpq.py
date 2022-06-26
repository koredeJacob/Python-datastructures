from array import ArrayType
import ctypes
from llqueue import llqueue


class boundedqueue:
    def __init__(self, numlevels):
        self._qsize = 0
        ArrayType = ctypes.py_object * numlevels
        self._qlevels = ArrayType()

        for i in range(numlevels):
            self._qlevels[i] = llqueue()

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self._qsize

    def enqueue(self, item, priority):
        assert priority >= 0 and priority < len(
            self._qlevels), "invalid priority level"
        self._qlevels[priority].enqueue(item)
        self._qsize += 1

    def dequeue(self):
        assert not self.isEmpty(), "cannot dequeue from an empty queue"
        i = 0
        p = len(self._qlevels)-1
        while i < p and not self._qlevels[i].isEmpty():
            i += 1
        self._qsize -= 1

        return self._qlevels[i].dequeue()


x = boundedqueue(3)
x.enqueue(1, 2)
x.enqueue(2, 0)
x.enqueue(3, 1)
print(x.isEmpty())
print(x.dequeue())
