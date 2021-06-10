import sys
sys.stdin = open('input (43).txt', 'r')


n = int(input())

arr = [[0] * n for _ in range(n)]
k = 0
p = 0
if n % 2:
    for j in range(n//2, -1, -1):
        p += 1
        for i in range(n // 2 - p + 1, n // 2 + p):
                k = k % 26
                arr[i][j] = chr(k + 65)
                k += 1

    else:
        for i in range(n):
            for j in range(n):
                if arr[i][j]:
                    print(arr[i][j], end=' ')
            print()
else:
    print('INPUT ERROR')
