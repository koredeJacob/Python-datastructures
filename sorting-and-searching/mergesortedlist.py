def mergelist(lst1,lst2):
    newlst=[]
    a,b=0,0
    
    while a<len(lst1) and b<len(lst2):
        if lst1[a]<lst2[b]:
            newlst.append(lst1[a])
            a+=1
        else:
            newlst.append(lst2[b])
            b+=1
    while a<len(lst1):
        newlst.append(lst1[a])
        a+=1
    while b<len(lst2):
        newlst.append(lst2[b])
        b+=1
    return newlst
print(mergelist([2,4,4,6],[3,4,7,9]))