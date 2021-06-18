
A = [2, 3, 1, 5]

cntA = [0] * 1000001
cntA[0] = 1

for i in A:
    cntA[i] = 1

print(cntA.index(0))