#modified binary search to return fitst occurence
def binarysearch(thevalue,target):
    low=0
    high=len(thevalue)-1

    while low<=high:
        mid=(low+high)//2

        if thevalue[mid]>target:
            high=mid-1
        elif thevalue[mid]<target:
            low=mid+1
        else:
            if mid>0 and thevalue[mid-1]==thevalue[mid]:
                high=mid-1
            else:
                return mid
    return -1
x=[0,1,2,2,2,3,4]
print(binarysearch(x,2))