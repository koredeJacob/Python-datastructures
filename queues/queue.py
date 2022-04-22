class Queue:
    def __init__(self):
        self._qlist=[]
        
    def length(self):
        return len(self._qlist)
    
    def isEmpty(self):
        return len(self._qlist)==0
    
    def enqueue(self,item):
        self._qlist.append(item)
        
    def dequeue(self):
        assert len(self._qlist)>0 ,"cannot remove from empty queue"
        self._qlist.pop(0)