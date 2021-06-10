import sys
sys.stdin = open('input (43).txt', 'r')


n = int(input())

arr = [[0] * n for _ in range(n)]

k = 0

for j in range(n):
    if j % 2:
        for i in range(n-1, -1, -1):
            k = k % 26
            arr[i][j] = chr(k+65)
            k += 1
    else:
        for i in range(n):
            k = k % 26
            arr[i][j] = chr(k+65)
            k += 1

for i in range(n):
    print(*arr[i])
