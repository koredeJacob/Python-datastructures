from queue import Empty


class Minheap:

    def __init__(self):
        self._elements = []

    def __len__(self):
        return len(self._elements)

    def isEmpty(self):
        return len(self) == 0

    def add(self, value):
        self._elements.append(value)
        self.siftup(len(self)-1)

    def siftup(self, index):
        parent = (index-1)//2
        if parent >= 0 and self._elements[parent] > self._elements[index]:
            self._elements[parent], self._elements[index] = self._elements[index], self._elements[parent]
            self.siftup(parent)

    def min(self):
        if self.isEmpty():
            raise Empty("priority queue is empty")
        return self._elements[0]

    def remove(self):
        if self.isEmpty():
            raise Empty("priority queue is empty")
        self._elements[0], self._elements[len(
            self._elements)-1] = self._elements[len(self._elements)-1], self._elements[0]
        min = self._elements.pop()
        self.siftdown(0)

        return min

    def siftdown(self, index):
        left = 2*index+1
        rigth = 2*index+2

        if left <= len(self._elements)-1:
            smallest = left
            if rigth <= len(self._elements)-1:
                if self._elements[left] > self._elements[rigth]:
                    smallest = rigth

            if self._elements[index] > self._elements[smallest]:
                self._elements[smallest], self._elements[index] = self._elements[index], self._elements[smallest]
                self.siftdown(smallest)


x = Minheap()
x.add(14)
x.add(12)
x.add(4)
x.add(5)
x.add(3)
print(x.min())
print(x.remove())
print(x.remove())
print(x.remove())
print(x.remove())
print(x.remove())
