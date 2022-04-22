def kthsmallest(s, k):
    if k < 0 or k > len(s):
        return None
    if len(s) == 1:
        return s[0]
    pivot = s[0]
    l = [x for x in s if x < pivot]
    e = [x for x in s if x == pivot]
    g = [x for x in s if x > pivot]

    if k <= len(l):
        return kthsmallest(l, k)
    elif k <= len(l)+len(e):
        return pivot
    j = k-len(l)-len(e)
    return kthsmallest(g, j)


arr = [4, 6, 3, 1, 0, 8, 8, 9, 4]
print(kthsmallest(arr, 1))
