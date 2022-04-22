def exp(x,n):
    if n==0:
        return 1
    if n%2==0:
        return exp(x*x,n//2)
    return x * exp(x*x,n//2)
print(exp(2,4))
