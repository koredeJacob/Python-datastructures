
def lcsLength(x, y):
    n, m = len(x), len(y)
    a = [[-1]*(m+1) for i in range(n+1)]

    lcs = memoizedlcs(a, x, y, n, m)
    print(solution(x, y, a), end="")
    return lcs


def memoizedlcs(a, x, y, n, m):
    if n == 0 or m == 0:
        a[n][m] = 0
    elif (a[n][m] != -1):
        return a[n][m]

    elif x[n-1] == y[m-1]:
        a[n][m] = memoizedlcs(a, x, y, n-1, m-1) + 1
    else:
        a[n][m] = max(memoizedlcs(a, x, y, n-1, m),
                      memoizedlcs(a, x, y, n, m-1))
    return a[n][m]


def tabulationlcs(x, y):
    n, m = len(x), len(y)
    a = [[0]*(m+1) for i in range(n+1)]

    for i in range(n):
        for j in range(m):
            if x[i] == y[j]:
                a[i+1][j+1] = a[i][j]+1
            else:
                a[i+1][j+1] = max(a[i+1][j], a[i][j+1])
    print(solution(x, y, a), end="")
    return a[n][m]


def solution(x, y, l):
    n, m = len(x), len(y)
    sol = []

    while l[n][m] > 0:
        if x[n-1] == y[m-1]:
            n -= 1
            m -= 1
            sol.append(x[n-1])
        elif l[n-1][m] >= l[n][m-1]:
            n -= 1
        else:
            m -= 1
    return "".join(reversed(sol))


print(lcsLength("CACBBBCCAABACABAABCABAACABBAAACDDDADAABA",
                "CBACDDACCAAAACCADACAACAADACADDAAAADDBABA"))
print(tabulationlcs("CACBBBCCAABACABAABCABAACABBAAACDDDADAABA",
                    "CBACDDACCAAAACCADACAACAADACADDAAAADDBABA"))
print(tabulationlcs("GTTCCTAATA", "CGATAATTGAGA"))
print(lcsLength("GTTCCTAATA", "CGATAATTGAGA"))
