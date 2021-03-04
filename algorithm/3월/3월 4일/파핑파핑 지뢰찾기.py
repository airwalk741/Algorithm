import sys

sys.stdin = open('input (43).txt', 'r')

def color(a, b):
    arr[i][j] = 'p'
    for k in range(9):
        dx = a + dr[k]
        dy = b + dc[k]
        if 0 <= dx < n and 0 <= dy < n:
            arr[dx][dy] = 'p'


T = int(input())

for tc in range(1, T+1):
    n = int(input())

    arr = [list(input()) for _ in range(n)]
    res = 0

    dr = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 0, 1, 1, 1, 0, -1, -1, -1]

    ping = 0
    cnt = 0

    for i in range(n):
        for j in range(n):
            for k in range(9):
                dx = i + dr[k]
                dy = j + dc[k]
                if 0 <= dx < n and 0 <= dy < n:

                    if arr[dx][dy] == '*':
                        break
            else:
                if arr[i][j] == 'p':
                    color(i, j)
                else:
                    res += 1
                    color(i, j)

    for i in range(n):
        for j in range(n):
            if arr[i][j] == '.':
                res += 1

    print('#{}'.format(tc), end=' ')
    print(res)













