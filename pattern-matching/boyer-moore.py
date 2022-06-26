def boyer_moore(t, p):
    n, m = len(t), len(p)
    if m == 0:
        return 0
    last = {}

    for i in range(m):
        last[p[i]] = i

    i = m-1
    k = m-1

    while i < n:
        if t[i] == p[k]:
            if k == 0:
                return i
            else:
                k -= 1
                i -= 1
        else:
            j = last.get(t[i], -1)
            i += m-min(k, j+1)
            k = m-1
    return -1


print(boyer_moore("korede", "re"))
