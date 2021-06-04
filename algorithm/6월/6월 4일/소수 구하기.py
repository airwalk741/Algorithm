import sys
sys.stdin = open('input (43).txt', 'r')


m, n = map(int, input().split())

arr = [1] * (n + 1)

arr[0] = 0
arr[1] = 0

for i in range(2, n+1):
    if arr[i]:
        j = 2
        k = i
        while i * j < n + 1:

            k = i * j

            arr[k] = 0

            j += 1

for i in range(m, n+1):

    if arr[i]:
        print(i)
