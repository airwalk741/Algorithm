import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs():
    global result

    q = deque()

    q.append((0, 0, arr[0][0]))

    while q:

        r, c, alpha = q.popleft()

        result = max(result, len(alpha))

        for i in range(4):
            x = dr[i] + r
            y = dc[i] + c

            if -1 < x < n and -1 < y < m:
                if arr[x][y] not in alpha:
                    q.append((x, y, alpha + arr[x][y]))



n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]

result = 0

bfs()

print(result)