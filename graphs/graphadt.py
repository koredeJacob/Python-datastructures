class Graph:

    class Vertex:
        __slots__ = "_element"

        def __init__(self, x):
            self._element = x

        def element(self):
            return self._element

        def __hash__(self):
            return hash(id(self))

    class Edge:
        __slots__ = "_origin", "_destination", "_element"

        def __init__(self, u, v, x):
            self._origin = u
            self._destination = v
            self._element = x

        def element(self):
            return self._element

        def endPoints(self):
            return (self._origin, self._destination)

        def opposie(self, v):
            return self._origin if v is self._destination else self._origin

        def __hash__(self):
            return hash((self._origin, self._destination))
