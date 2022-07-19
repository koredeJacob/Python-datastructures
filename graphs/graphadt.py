from collections import deque
from copy import deepcopy


class Graph:

    def __init__(self, directed=False):
        self.outgoing = {}
        self.incoming = {} if directed else self.outgoing

    def isDirected(self):
        return self.outgoing is not self.incoming

    def vertexCount(self):
        return len(self.outgoing)

    def vertices(self):
        return self.outgoing.keys()

    def edgeCount(self):
        total = 0
        for i in self.outgoing:
            total += len(self.outgoing[i])
        return total if self.isDirected else total//2

    def degree(self, v, outgoing=True):
        if outgoing:
            return len(self.outgoing[v])
        return len(self.incoming[v])

    def edges(self):
        edgeset = set()
        for i in self.outgoing.values():
            edgeset.update(i.values())
        return edgeset

    def getEdge(self, u, v):
        incident = self.outgoing.get(u)
        if incident:
            return incident.get(v)

    def incidentEdges(self, v, outgoing=True):
        adj = self.outgoing[v] if outgoing else self.incoming[v]

        for edge in adj.values():
            yield edge

    def insertVertex(self, x=None):
        vertex = self.Vertex(x)
        self.outgoing[vertex] = {}
        if self.isDirected():
            self.incoming[vertex] = {}
        return vertex

    def insertEdge(self, u, v, x=None):
        edge = self.Edge(u, v, x)
        self.outgoing[u][v] = edge
        self.incoming[v][u] = edge

    def removeVertex(self, v):
        outgoingv = self.outgoing[v]
        for i in outgoingv:
            del self.incoming[i][v]
        del outgoingv

    def removeEdge(self, e):
        origin, destination = e.endpoints()
        del self.outgoing[origin][destination]
        del self.incoming[destination][origin]

    def dfs(self, u, discovered):

        for e in self.incidentEdges(u):
            v = e.opposite(u)
            if v not in discovered:
                discovered[v] = e
                self.dfs(v, discovered)

    def isConnected(self, u, v, discovered):
        path = []
        if v in discovered:
            path.append(v)
            walk = v
            while walk is not u:
                e = discovered[walk]
                parent = e.opposite(walk)
                path.append(parent)
                walk = parent
            path.reverse()
        return path

    def dfsComplete(self):
        forest = {}
        for u in self.vertices():
            if u not in forest:
                forest[u] = None
                self.dfs(u, forest)

        return forest

    def bfs(self, u, discovered):
        q = deque()
        q.append(u)

        while len(q) > 0:
            v = q.popleft()
            for e in self.incidentEdges(v):
                opp = e.opposite(v)
                if opp not in discovered:
                    discovered[opp] = e
                    q.append(opp)

    def floydWarshall(self):
        closure = deepcopy(self)
        verts = list(self.vertices())
        n = len(verts)

        for k in range(n):
            for i in range(n):
                if i != k and closure.getEdge(verts[i], verts[k]) is not None:
                    for j in range(n):
                        if i != j != k and closure.get_edge(verts[k], verts[j]) is not None:

                            if closure.getEdge(verts[i], verts[j]) is None:
                                closure.insertEdge(verts[i], verts[j])
        return closure

    def topologicalSort(self):
        topo = []
        ready = []
        incount = {}

        for v in self.vertices():
            incount[v] = self.degree(v, False)
            if incount[v] == 0:
                ready.append(v)

        while len(ready) > 0:
            u = ready.pop()
            for e in self.incidentEdges(u):
                v = e.opposite(u)
                incount[v] -= 1
                if incount[v] == 0:
                    ready.append(v)
            topo.append(u)
        return topo

#    def dijsktra(G,s):
#       d={}
#       cloud={}
#       pq=adaptablepq()
#       pqlocator={}
#
#       for i in G.vertices():
#           if i is s:
#               d[i]==0
#           else:
#               d[i]=float("inf")
#           pqlocator[i]=pq.add(d[i],i)
#
#      while not pq.isEmpty():
#           key,u=pq.removemin()
#           cloud[u]=key
#           del pqlocator[u]
#           for e in G.incidentedges(u):
#               v=e.opposite(u)
#               if v not in cloud:
#                   if d[u]+e.element()<d[v]:
#                       d[v]=d[u]+e.element
#                       pq.update(pqlocator[v],d[v],v)
#       return cloud

#       def shortestpathtree(g,s,d):
#           tree={}
#           for u in d:
#               if u not s:
#                   for e in g.incidentEdges(u,False):
#                       if d[u]=e.element+d[e.opposite(u)]:
#                           tree[u]=e
#           return tree

#   def primjanik(g):
#       d={}
#       pq=adaptablepriorityqueue()
#       pqlocator={}
#       tree=[]
#
#       for u in g.vertices():
#           if len(d)==0:
#               d[u]=0
#           else:
#               d[u]=float('inf')
#           pqlocator[u]=pq.add(d[u],(v,None))
#
#       while not pq.isEmpty:
#           key,value=pq.remove_min()
#           u,e=value
#           if edge is not None:
#               tree.append(e)
#           del pqlocator[u]
#
#           for link in g.incidentEdges(u):
#               v=link.opposite(u)
#               if link.element()<d[v]:
#                   d[v]=link.element
#                   pq.update(pqlocator[v],d[v],(v,link)
#       return tree

#   def kruskal(g):
#       tree=[]
#       pq=heappriorityqueue()
#       forest=partition()
#       position={}
#
#       for v in g.vertices():
#           position[v]=forest.makegroup(v)
#
#       for e in g.edges():
#           pq.add(e.element,e)
#
#       size=g.vertexcount()
#
#       while len(tree)!=size -1 and not pq.isEmpty():
#
#           weight,edge=pq.removemin()
#           u,v=edge.enpoints()
#           a=forest.find(position[u])
#           b=forest.find(position[v])
#           if a!b:
#               tree.append(edge)
#               forest.union(a,b)
#
# return tree


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

    def opposite(self, v):
        return self._origin if v is self._destination else self._origin

    def __hash__(self):
        return hash((self._origin, self._destination))
