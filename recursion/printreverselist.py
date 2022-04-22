def printlist(node):
    if node is not None:
        printlist(node.next)
        print(node.data)