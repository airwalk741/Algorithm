
A = [-1000, 1000]

result = []

front = 0
back = sum(A)

for i in range(len(A) - 1):

    front += A[i]
    back -= A[i]

    result.append(abs(front - back))

return min(result)