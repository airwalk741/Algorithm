import sys

sys.stdin = open('input (43).txt', 'r')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def root(r, c, cnt, k):
    global result

    if result < cnt:
        result = cnt

    for i in range(4):
        x = r + dr[i]
        y = c + dc[i]
        if -1 < x < n and -1 < y < n:
            if mount[x][y] < mount[r][c] and visited[x][y] == 0:
                visited[x][y] = 1
                root(x, y, cnt + 1, k)
                visited[x][y] = 0
            elif mount[x][y] >= mount[r][c] and visited[x][y] == 0:
                j = 1
                k2 = k
                while k > 0:
                    k -= 1
                    if mount[x][y] - j < mount[r][c] and visited[x][y] == 0:
                        visited[x][y] = 1
                        root(x, y, cnt + 1, k)
                        visited[x][y] = 0
                        break
                    j += 1
                k = k2


T = int(input())

for tc in range(1, T+1):

    n, k = map(int, input().split())

    mount = [ list(map(int, input().split())) for _ in range(n)]

    visited = [[0] * n for _ in range(n)]


    max_h = 0

    for i in range(n):
        if max_h < max(mount[i]):
            max_h = max(mount[i])

    result = 0

    for i in range(n):
        for j in range(n):
            if mount[i][j] == max_h:
                visited[i][j] = 1
                root(i, j, 0, k)
                visited[i][j] = 0

    print(result)









