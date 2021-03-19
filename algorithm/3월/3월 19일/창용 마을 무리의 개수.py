import sys

sys.stdin = open('input (43).txt', 'r')

def dfs(r, c):
    global cnt
    s = []
    s.append([r, c])

    while len(s):
        x, y = s.pop()

        if arr[x][y]:
            arr[x][y] = 0

            for i in range(n+1):
                if arr[y][i]:
                    s.append([y, i])
                if arr[i][y]:
                    s.append([i, y])
                if arr[x][i]:
                    s.append([x, i])
                if arr[i][x]:
                    s.append([i, x])

    cnt += 1

T = int(input())

for tc in range(1, T+1):

    print('#{}'.format(tc), end=' ')

    n, m = map(int, input().split())

    arr = [[0] * (n+1) for _ in range(n+1)]

    num = []

    for i in range(m):
        num += map(int, input().split())

    no_num = [0] * (n+1)


    for i in range(len(num)):
        no_num[num[i]] += 1

    cnt = no_num.count(0) - 1

    for i in range(0, len(num), 2):
        arr[num[i]][num[i+1]] = 1

    for i in range(n+1):
        for j in range(n+1):
            if arr[i][j]:
                dfs(i, j)

    print(cnt)
