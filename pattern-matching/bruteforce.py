def find_brute(t, p):
    n, m = len(t), len(p)

    for i in range(n-m+1):
        k = 0
        while k < m and t[k+i] == p[k]:
            k += 1
        if k == m:
            return i
    return -1


print(find_brute("korede", "e"))
