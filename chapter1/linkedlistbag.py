from listnode import ListNode
class Bag:
    def __init__(self):
        self._head=None
        self._size=0

    def __len__(self):
        return self._size

    def __contain__(self,data):
        currentnode=self._head
        while currentnode is not None:
            if currentnode.data=data:
                return True
        return False
    
    def add(self,data):
        currentnode=ListNode(data)
        currentnode.next=self._head
        self._head=currentnode
        self._size+=1

    def remove(self,item):
        prednode=None
        currentnode=self._head
        while currentnode is not None and currentnode.data!=item:
            prednode=currentnode
            currentnode=currentnode.next

        assert currentnode is not None,"the item must be in the bag"
        self._size-=1
        if currentnode==self._head:
            self._head=currentnode.next
        else:
            prednode.next=currentnode.next
        return current.data

    def __iter__(self):
        return _BagIterator(self._head)

class __BagIterator__(self):
    def __init__(self,listhead):
        self._curnode=listhead
    
    def __iter__():
        return self
    def __next__():
        if self._currnode is None:
            raise StopIteration
        else:
            item=self._currnode.data
            self._currnode=self._currnode.next
            return item


    


            
        
    