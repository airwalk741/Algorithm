import sys
sys.stdin = open('input (43).txt', 'r')
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def pipe(num):

    if num == 1:
        return [0, 1, 2, 3]
    elif num == 2:
        return [0, 2]
    elif num == 3:
        return [1, 3]
    elif num == 4:
        return [0, 1]
    elif num == 5:
        return [1, 2]
    elif num == 6:
        return [2, 3]
    elif num == 7:
        return [0, 3]

def bfs(r, c):
    global l

    cnt = 1
    q = deque()
    q.append((r, c, 1))
    visited[r][c] = 1

    while q:

        nx, ny, time = q.popleft()

        if time == l:
            return cnt

        now_pipe = pipe(arr[nx][ny])

        for i in now_pipe:
            x = nx + dr[i]
            y = ny + dc[i]
            if -1 < x < n and -1 < y < m and visited[x][y] == 0:
                if i == 0:
                    if arr[x][y] in [1, 2, 5, 6]:
                        visited[x][y] = 1
                        cnt += 1
                        q.append((x, y, time+1))
                elif i == 1:
                    if arr[x][y] in [1, 3, 6, 7]:
                        visited[x][y] = 1
                        cnt += 1
                        q.append((x, y, time+1))
                elif i == 2:
                    if arr[x][y] in [1, 2, 4, 7]:
                        visited[x][y] = 1
                        cnt += 1
                        q.append((x, y, time+1))
                elif i == 3:
                    if arr[x][y] in [1, 3, 4, 5]:
                        visited[x][y] = 1
                        cnt += 1
                        q.append((x, y, time+1))

    return cnt

T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    n, m, r, c, l = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    visited = [[0] * m for _ in range(n)]

    result = bfs(r, c)

    print(result)

