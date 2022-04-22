def quicksort(s, a, b):
    if a >= b:
        return
    pivot = s[b]
    left = a
    right = b-1

    while left <= right:
        while left <= right and s[left] < pivot:
            left += 1
        while left <= right and s[right] > pivot:
            right -= 1
        if left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    s[left], s[b] = s[b], s[left]

    quicksort(s, a, left-1)
    quicksort(s, left+1, b)


x = [9, 3, 5, 6, 2, 1, 0, 8]
quicksort(x, 0, len(x)-1)
print(x)
