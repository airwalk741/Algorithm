import sys
sys.stdin = open('input (43).txt', 'r')


n = int(input())

arr = [[0] * n for _ in range(n)]
k = 0
m = 0
i = 0
j = n -1
q = 0
while True:

    k = k % 26

    arr[i][j] = chr(k + 65)

    if i == n-1 and j == n-1:
        break

    i += 1
    j -= 1

    if i == n:
        q += 1
        i = q
        j = n - 1

    k += 1

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            print(arr[i][j], end=' ')
        else:
            print(end='  ')
    print()