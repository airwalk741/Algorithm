import sys
sys.stdin = open('input (43).txt', 'r')

from collections import deque
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(r, c):

    q = deque()
    q.append((r, c))

    while q:

        r, c = q.popleft()

        for i in range(4):
            x = r + dr[i]
            y = c + dc[i]

            if -1 < x < n and -1 < y < n:
                if visited[x][y] > visited[r][c] + arr[r][c]:
                    visited[x][y] = visited[r][c] + arr[r][c]
                    q.append((x, y))

T = int(input())

for tc in range(1, T+1):

    n = int(input())

    arr = [list(map(int, input())) for _ in range(n)]

    visited = [[987654321] * n for _ in range(n)]

    visited[0][0] = 0

    bfs(0, 0)

    print('#{} {}'.format(tc, visited[-1][-1]))
