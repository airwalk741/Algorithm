import sys
sys.stdin = open('input (43).txt', 'r')
input = sys.stdin.readline
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 최단거리 BFS
def bfs(r, c):

    q = deque()
    q.append((r, c))
    while q:

        num = q.popleft()
        for i in range(4):
            x = num[0] + dr[i]
            y = num[1] + dc[i]
            if -1 < x < n and -1 < y < m:
                if visited[x][y] == 0 and arr[x][y] == 1:
                    visited[x][y] = visited[num[0]][num[1]] + 1
                    q.append((x, y))


def bfs2(r, c):
    pass

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]


# 시작점 찾기
for i in range(n):
    if 2 in arr[i]:
        r, c = (i, arr[i].index(2))
        break

visited = [[0] * m for _ in range(n)]

bfs(r, c)


for i in range(n):
    for j in range(m):
        # 울타리 속 가지 못했던 곳
        if arr[i][j] != 2 and arr[i][j] != 0 and visited[i][j] == 0:
            print('-1', end=' ')
        else:
            print(visited[i][j], end=' ')
    print()