import sys
sys.stdin = open('input (43).txt', 'r')

dr = [0, 1]
dc = [1, 0]

def dfs():

    s = [(0, 0)]

    while s:

        r, c = s.pop()

        for i in range(2):
            x = dr[i] + r
            y = dc[i] + c

            if -1 < x < n and -1 < y < n:
                if visited[x][y] > visited[r][c] + arr[x][y]:
                    visited[x][y] = visited[r][c] + arr[x][y]
                    s.append((x, y))

T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    visited = [[987654321] * n for _ in range(n)]

    visited[0][0] = arr[0][0]

    dfs()

    print(visited[-1][-1])