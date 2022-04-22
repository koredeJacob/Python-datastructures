def gcd(a,b,c):
    if a%c==0 and b%c==0:
        return c
    return gcd(a,b,c-1)
print(gcd(9,6,6))
