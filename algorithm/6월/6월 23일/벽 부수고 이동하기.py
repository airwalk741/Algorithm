import sys
sys.stdin = open('input (43).txt', 'r')
from collections import deque

# 3차원 방문체크로 벽을 격파 할 수 있는지 없는지에 따라 최소 거리를 구한다.

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(r, c, cnt):

    q = deque()
    q.append((r, c, cnt))

    while q:

        r, c, cnt = q.popleft()

        for i in range(4):
            x = r + dr[i]
            y = c + dc[i]

            if -1 < x < n and -1 < y < m:
                # 벽이 아닐때
                if not arr[x][y]:
                    # 벽을 격파 할 수 있을 때
                    if not cnt:
                        if visited[x][y][1] > visited[r][c][1] + 1:
                            visited[x][y][1] = visited[r][c][1] + 1
                            q.append((x, y, cnt))
                    # 벽을 격파할 수 없을 때
                    else:
                        if visited[x][y][0] > visited[r][c][0] + 1:
                            visited[x][y][0] = visited[r][c][0] + 1
                            q.append((x, y, cnt))

                # 벽이면서 벽을 격파 할 수 있을 때
                if cnt:
                    if visited[x][y][1] > visited[r][c][0] + 1:
                        visited[x][y][1] = visited[r][c][0] + 1
                        q.append((x, y, 0))


n, m = map(int, input().split())

arr = [list(map(int, input())) for _ in range(n)]

visited = [[[987654321 for _ in range(2)]for _ in range(m)] for _ in range(n)]

visited[0][0][0] = 1

bfs(0, 0, 1)

_min = 987654321
for value in visited[n -1][m - 1]:
    if value:
        if _min > value:
            _min = value

if _min != 987654321:
    print(_min)
else:
    print(-1)



