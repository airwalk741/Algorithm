import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
import pprint

## 먼저 하나의 위치에서 BFS를 돌리고 기록이 갱신 될때마다 현 위치 좌표를 담는다.
## 위치 담은 좌표들을 다시 BFS를 돌려 최대 처리를 구한다.

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(r, c):
    global first_dist
    global first


    q = deque()
    q.append((r, c, 0))


    while q:

        r, c, dist = q.popleft()

        if dist > first_dist:
            first_dist = dist
            first.append((r, c))

        for i in range(4):

            x = r + dr[i]
            y = c + dc[i]

            if -1 < x < n and -1 < y < m:
                if not visited[x][y]:
                    if arr[x][y] == 'L':
                        visited[x][y] = visited[r][c] + 1
                        q.append((x, y, visited[x][y]))



n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]

first_dist = 0
first = []

visited = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if arr[i][j] == 'L':
                visited[i][j] = 1
                bfs(i, j)

first_dist = 0

second = []
length = len(first)
pprint.pprint(visited)
print(first)

for i in range(length):

    r, c = first[i][0], first[i][1]
    first_dist = 0
    visited = [[0] * m for _ in range(n)]
    visited[r][c] = 1
    bfs(r, c)
    second.append(first_dist)


print(max(second) - 1)

