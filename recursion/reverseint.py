def printrev(n):
    if n>0:
        print(n)
        printrev(n-1)
def printinc(n):
    if n>0:
        printinc(n-1)
        print(n)
printinc(6)
printrev(9)