from listnode import ListNode


class SLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        currentnode = self.head
        while currentnode is not None:
            print(currentnode.data)
            currentnode = currentnode.next

    def unorderedsearch(self, target):
        currentnode = self.head
        while currentnode is not None:
            if currentnode.data == target:
                return True
            currentnode = currentnode.next
        return False

    def prepend(self, data):
        newnode = ListNode(data)
        newnode.next = self.head
        self.head = newnode

    def remove(self, data):
        prevnode = None
        currentnode = self.head
        while currentnode is not None and currentnode.data != data:
            prevnode = currentnode
            currentnode = currentnode.next
        if currentnode is not None:
            if currentnode == self.head:
                self.head = currentnode.next
            else:
                prevnode.next = currentnode.next

    def orderedsearch(self, data):
        currentnode = self.head

        while currentnode is not None and currentnode.data <= data:
            if currentnode.data == data:
                return True
            currentnode = currentnode.next
        return False

    def insertsorted(self, data):
        prednode = None
        currentnode = self.head
        while currentnode is not None and currentnode.data <= data:
            prednode = currentnode
            currentnode = currentnode.next

        newnode = ListNode(data)

        if currentnode is self.head:
            newnode.next = self.head
            self.head = newnode
        else:
            prednode.next = newnode
            newnode.next = currentnode


x = SLinkedList()
x.prepend(5)
x.prepend(4)
x.traverse()
