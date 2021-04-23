import sys
sys.stdin = open('input (43).txt', 'r')

import heapq
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(r, c):

    q = []
    heapq.heappush(q, (r, c, 0))
    while q:
        r, c, w = heapq.heappop(q)

        for i in range(4):
            x = r + dr[i]
            y = c + dc[i]
            if -1 < x < n and -1 < y < n:
                if visited[x][y] > w + arr[x][y]:
                    visited[x][y] = w + arr[x][y]
                    heapq.heappush(q, (x, y, visited[x][y]))

T = int(input())

for tc in range(1, T+1):

    n = int(input())

    arr = [list(map(int, input())) for _ in range(n)]

    visited = [[987654321] * n for _ in range(n)]
    visited[0][0] = 0

    bfs(0, 0)

    print('#{} {}'.format(tc, visited[-1][-1]))




