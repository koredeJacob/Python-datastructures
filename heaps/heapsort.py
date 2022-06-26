from arrayheap import Minheap
from heapq import *

v = [8, 7, 4, 5, 3, 8]
heapify(v)
print(nsmallest(3, v))
print(v)


def heapsort(seq):
    n = len(seq)
    heap = Minheap()

    for i in seq:
        heap.add(i)

    for i in range(n):
        seq[i] = heap.remove()


def inplaceheapsort(seq):
    n = len(seq)

    def siftup(seq, i):
        parent = (i-1)//2
        if parent >= 0 and seq[parent] < seq[i]:
            seq[parent], seq[i] = seq[i], seq[parent]
            siftup(seq, parent)

    def siftdown(seq, root, stop):
        left = 2*root+1
        rigth = 2*root+2

        if stop-1 >= 0 and left <= stop-1:
            largest = left
            if rigth <= stop-1 and seq[left] <= seq[rigth]:
                largest = rigth
            if seq[root] < seq[largest]:
                seq[root], seq[largest] = seq[largest], seq[root]
                siftdown(seq, largest, stop)

    for i in range(1, n):
        siftup(seq, i)

    for j in range(n):
        seq[0], seq[n-(j+1)] = seq[n-(j+1)], seq[0]
        siftdown(seq, 0, n-(j+1))


n = [5, 2, 3, 9, 1, 0, 0, 4, 7]
heapsort(n)
x = [5, 2, 3, 9, 1, 0, 0, 4, 40, 3]
inplaceheapsort(x)
print(n, " ", x)
