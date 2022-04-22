class llqueue:
    def __init__(self):
        self.count=0
        self._qhead=None
        self._qtail=None
    def isEmpty(self):
        return self._qhead==None
    def __len__(self):
        return self.count
    def enqueue(self,item):
        node=Qnode(item)
        if self.isEmpty():
            self._qhead=node
        else:
            self._qtail.next=node
        
        self._qtail=node
        self.count+=1
    
    def dequeue(self):
        assert not self.isEmpty(),"cant remove from empty list"
        node=self._qhead
        if self._qhead is self._qtail:
            self._qtail=None
            
        self._qhead=self._qhead.next
        self.count-=1
        return node.item
class Qnode(object):
    def __init__(self,item):
        self.item=item
        self.next=None
        
               
    