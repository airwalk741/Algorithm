import sys
from collections import deque
sys.stdin = open('input (43).txt', 'r')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


T = int(input())

for tc in range(1, T + 1):

    n, m = map(int, input().split())

    arr = [list(input()) for _ in range(n)]

    visited = [[-1] * m for _ in range(n)]

    q = deque()

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                visited[i][j] = 0
                q.append((i, j))

    result = 0
    # result = bfs(q)
    while q:

        num = q.popleft()

        for i in range(4):
            x = num[0] + dr[i]
            y = num[1] + dc[i]

            if -1 < x < n and -1 < y < m:
                if visited[x][y] == -1:
                    visited[x][y] = visited[num[0]][num[1]] + 1
                    q.append((x, y))


    for i in range(n):
        result += sum(visited[i])

    print('#{}'.format(tc), end=' ')
    print(result)
