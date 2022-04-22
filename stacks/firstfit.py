def firstFit(blockSize, m, processSize, n):
    allocation = [-1] * n

    for i in range(n):
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                allocation[i] = j
                blockSize[j] -= processSize[i]

                break

    print(" Process No. Process Size      Block no.")
    for i in range(n):
        print(" ", i + 1, "         ", processSize[i],
                          "         ", end=" ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")


blockSize = [100, 500, 200, 300, 600]
processSize = [222, 427, 117, 416]
m = len(blockSize)
n = len(processSize)

firstFit(blockSize, m, processSize, n)

def bestFit(blockSize, m, processSize, n):
    allocation = [-1] * n
    for i in range(n):
        bestIndx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if bestIndx == -1:
                    bestIndx = j
                elif blockSize[bestIndx] > blockSize[j]:
                    bestIndx = j
        if bestIndx != -1:
            allocation[i] = bestIndx
            blockSize[bestIndx] -= processSize[i]

    print("Process No. Process Size     Block no.")
    for i in range(n):
        print(i + 1, "         ", processSize[i],
              end="         ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")


blockSize = [100, 500, 200, 300, 600]
processSize = [212, 417, 112, 426]
m = len(blockSize)
n = len(processSize)
bestFit(blockSize, m, processSize, n)

