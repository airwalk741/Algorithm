import sys
sys.stdin = open('input (43).txt', 'r')
from collections import deque
input = sys.stdin.readline
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(r, c):

    q = deque()
    q.append((r, c))

    while q:

        num = q.popleft()

        for i in range(4):

            x = num[0] + dr[i]
            y = num[1] + dc[i]

            if -1 < x < n and -1 < y < m:
                if arr[x][y]:
                    q.append((x, y))
                    arr[x][y] = 0

T = int(input())

for _ in range(T):

    m, n, k = map(int, input().split())

    arr = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())

        arr[y][x] = 1

    result = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                result += 1
                bfs(i, j)

    print(result)