def selectionsort(seq):
    n=len(seq)
    for i in range(n-1):
        min=seq[i]
        minindex=i

        for j in range(i+1,n):
            if min>seq[j]:
                min=seq[j]
                minindex=j
        if minindex!=i:
            temp=min
            seq[minindex]=seq[i]
            seq[i]=temp
    return seq
print(selectionsort([3,7,2,1,8,5,9,5]))