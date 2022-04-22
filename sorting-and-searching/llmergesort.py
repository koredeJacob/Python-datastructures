class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def llmergesort(lst):
    if lst is None:
        return None
    if not lst.next:
        return lst
    mid = lst
    current = mid.next
    while current is not None:
        current = current.next
        if current:
            current = current.next
            mid = mid.next
    rigth = mid.next
    mid.next = None
    left = lst
    leftrec = llmergesort(left)
    rigthrec = llmergesort(rigth)

    lst = merge(leftrec, rigthrec)

    return lst


def merge(first, second):
    dummy = ListNode(None)
    newlst = dummy
    while (first is not None) and (second is not None):
        if first.data <= second.data:
            newlst.next = first
            first = first.next
        else:
            newlst.next = second
            second = second.next
        newlst = newlst.next
        newlst.next = None
    if first is not None:
        newlst.next = first
    elif second is not None:
        newlst.next = second
    return dummy.next


x = ListNode(4)
y = ListNode(2)
z = ListNode(1)
b = ListNode(3)


x.next = y
y.next = z
z.next = b
print(x.data, x.next.data, x.next.next.data, x.next.next.next.data)
g = llmergesort(x)
print(g.data, g.next.data, g.next.next.data, g.next.next.next.data)
