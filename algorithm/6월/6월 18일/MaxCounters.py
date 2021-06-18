
A = [3, 4, 4, 6, 1, 4, 4]
N = 5

result = [0] * N
fakeMax = 0
realMax = 0

for i in range(len(A)):

    if A[i] == N + 1:
        realMax = fakeMax

    else:

        if result[A[i] - 1] < realMax:
            result[A[i] - 1] = realMax

        result[A[i] - 1] += 1

        if fakeMax < result[A[i] - 1]:
            fakeMax = result[A[i] - 1]

for i in range(N):

    if result[i] < realMax:
        result[i] = realMax

    return result