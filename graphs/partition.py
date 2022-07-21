from turtle import position


class Partition:

    class Position:

        __slots__ = '_container', '_element', '_size', '_parent'

        def __init__(self, container, e):
            self._container = container
            self._element = e
            self._size = 1
            self._parent = self

        def element(self):
            return self._element

    def make_group(self, x):
        return self.Position(self, x)

    def find(self, p):
        if p._parent != p:
            p._parent = self.find(p._parent)
        return p._parent

    def union(self, p, q):
        a = self.find(p)
        b = self.find(q)

        if a is not b:
            if a._size > b._size:
                b._parent = a
                a._size += b._size
            else:
                a._parent = b
                b._size += a._size
