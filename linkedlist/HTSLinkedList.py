class HTSLinkedList:
    def __init__(self,data):
        self._head=None
        self._tail=None
        self._size=0

    def append(self,data):
        newnode=ListNode(data)
        if self._head is None:
            self._head=newnode
        else:
            self._tail.next=newnode
        self._tail=newnode
        self.size+=1
    
    def remove(self,data):
        prednide=None
        currnode=ListNode(data)

        while currnode is not None and currnode.data!=target:
            prednode=currnode
            currnode=currnode.next
        
        if currnode is not None:
            if currnode==head:
                self._head=currnode.next
            else:
                prednode.next=currnode.next
            if currnode==self._tail:
                self._tail=prednode
        self._size-=1
