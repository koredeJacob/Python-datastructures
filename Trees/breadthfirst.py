from queues.llqueue import llqueue


def bfs(btree):
    q = llqueue()
    q.enqueue(btree)

    while q:
        node = q.dequeue()
        print(node.data)

        if node.left:
            q.enqueue(node.left)
        if node.rigth:
            q.enqueue(node.rigth)
