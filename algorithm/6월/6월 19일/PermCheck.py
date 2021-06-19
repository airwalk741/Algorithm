

A = [4, 1, 3, 2]


length = len(A)

permA = [0] * (length)

for i in range(length):

    try:
        permA[A[i] - 1] = 1
    except:
        return 0

if 0 in permA:
    return 0
else:
    return 1