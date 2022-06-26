def find_kmp(t, p):
    n, m = len(t), len(p)
    if m == 0:
        return 0
    fail = computefail(p)
    k, j = 0, 0

    while j < n:
        if t[j] == p[k]:
            if k == m-1:
                return j-m+1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return -1


def computefail(p):
    m = len(p)
    fail = [0]*m
    j = 1
    k = 0
    while j < m:
        if p[j] == p[k]:
            fail[j] = k+1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return fail


print(find_kmp("korede", "e"))
