import sys
from collections import deque
import copy
sys.stdin = open('input (43).txt', 'r')

input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(q):
    global result

    arr = copy.deepcopy(first_arr)

    virus = deque(q)

    while virus:

        x, y = virus.popleft()
        for i in range(4):
            r = x + dr[i]
            c = y + dc[i]

            if -1 < r < n  and -1 < c < m:
                if arr[r][c] == 0:
                    virus.append((r, c))
                    arr[r][c] = 2
    cnt = 0
    for i in arr:
        cnt += i.count(0)

    if result < cnt:
        result = cnt


def wall(cnt, arr):


    if cnt == 3:

        bfs(q)

    else:
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    wall(cnt + 1, arr)
                    arr[i][j] = 0


n, m = map(int, input().split())

first_arr = [list(map(int, input().split())) for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if first_arr[i][j] == 2:
            q.append((i, j))


result = 0

wall(0, first_arr)

print(result)

