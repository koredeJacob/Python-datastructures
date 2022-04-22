import array
    
class Queue:
    def __init__(self,maxsize):
        self._Aqueue=array(maxsize)
        self.count=0
        self.front=0
        self.back=len(self._Aqueue)-1
    
    def isEmpty(self):
        return self.count==0

    def isFull(self):
        return self.count==len(self._Aqueue)\
    
    def enqueue(self,item):
        assert not self.isFull(),"cannot enqueue toa full queue"
        maxsize=len(self._Aqueue)
        self.back=(self.back+1)%maxsize
        self._Aqueue[self.back]=item
        self.count+=1
    
    def dequeue(self):
        assert not self.isEmpty(),"cannot dequeue from an empty queue"
        item=self._Aqueue[self.front]
        maxsize=len(self._Aqueue)
        self.front=(self.front-1)%maxsize
        self.count-=1
        return item
    