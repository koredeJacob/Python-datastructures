def rodcutting(p, n):
    if n == 0:
        return 0
    q = -1
    for i in range(1, n+1):
        q = max(q, p[i]+rodcutting(p, n-i))
    return q


def memoizedrodcut(p, n):
    r = [-1]*(n+1)
    return memoizedrodcutaux(p, n, r)


def memoizedrodcutaux(p, n, r):
    if r[n] >= 0:
        return r[n]
    elif n == 0:
        r[n] = 0
        return r[n]
    q = -1
    for i in range(1, n+1):
        q = max(q, p[i]+memoizedrodcutaux(p, n-i, r))
    r[n] = q
    return r[n]


def bottomupcutrod(p, n):
    r = [0]*(n+1)
    s = [0]*(n+1)
    for i in range(1, n+1):
        q = -1
        for j in range(1, i+1):
            if q < p[j]+r[i-j]:
                q = p[j]+r[i-j]
                s[i] = j
        r[i] = q
    return r, s


def printcutrod(p, n):
    r, s = bottomupcutrod(p, n)
    while n > 0:
        print(s[n], end=" ")
        n -= s[n]


print(rodcutting([0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 4))
print(memoizedrodcut([0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 7))
printcutrod([0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 7)
