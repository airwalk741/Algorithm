import sys
sys.stdin = open('input (43).txt', 'r')


n = int(input())
# 65 ~ 90

arr = [[0] * n for _ in range(n)]
k = 0
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        k = k % 26
        arr[j][i] = chr(k + 65)
        k += 1

for i in range(n):
    print(*arr[i])