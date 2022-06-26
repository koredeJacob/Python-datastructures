def matrixchainprod(p):
    n = len(p)-1

    m = [[0]*n for l in range(n)]

    for i in range(1, n):
        for b in range(n-i):
            j = i+b
            for k in range(i, j):
                m[i][j] = min(m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1])

    return m
