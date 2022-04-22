def insertionsort(theseq):
    for i in range(1, len(theseq)):
        value = theseq[i]
        pos = i

        while pos > 0 and value < theseq[pos-1]:
            theseq[pos] = theseq[pos-1]
            pos -= 1
        theseq[pos] = value
    return theseq


print(insertionsort([8, 7, 4, 9, 2, 1, 4, 8, 5, 3]))
