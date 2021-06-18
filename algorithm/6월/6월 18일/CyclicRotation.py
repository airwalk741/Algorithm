

A = [3, 8, 9, 7, 6]
K = 3
length = len(A)

K = K % length

result = [0] * length

for i in range(length):

    if i + K >= length:
        nextIdx = (i + K) % length
        result[nextIdx] = A[i]
    else:
        result[i + K] = A[i]

print(result)
