class PriorityQueue:
    def __init__(self):
        self._qlist=[]
        
    def isEmpty(self):
        return len(self._qlist)==0
    
    def __len__(self):
        return len(self._qlist)
    def enqueue(self,item,priority):
        self._qlist.append(pqEntry(item,priority))
    def dequeue(self):
        assert not self.isEmpty(),"cant dequeue empty queue"
        highest=self._qlist[0].priority
        x=0
        for i in range(1,len(self._qlist)):
            if self._qlist[i].priority<highest:
                highest=self._qlist[i].priority
                x=i
        entry=self._qlist.pop(x)
        return entry.item
class pqEntry(object):
    def __init__(self,item,priority):
        self.item=item
        self.priority=priority
        
x=PriorityQueue()
x.enqueue(1,5)
x.enqueue(5,5)
x.enqueue(2,5)
print(x.dequeue())
 
        