def mergesort(s):
    n = len(s)
    if n < 2:
        return
    mid = n//2
    s1 = s[0:mid]
    s2 = s[mid:n]

    mergesort(s1)
    mergesort(s2)

    merge(s1, s2, s)


def merge(s1, s2, s):
    i = j = 0
    while i+j < len(s):
        if j == len(s2) or i < len(s1) and s1[i] < s2[j]:
            s[i+j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1


x = [5, 3, 8, 6, 2, 9]
mergesort(x)
print(x)
