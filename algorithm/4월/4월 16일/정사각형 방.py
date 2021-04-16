import sys
sys.stdin = open('input (43).txt', 'r')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')

    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    visited = [0] * ((n * n) + 1)

    for i in range(n):
        for j in range(n):
            for k in range(4):
                r = i + dr[k]
                c = j + dc[k]
                if -1 < r < n and -1 < c < n:
                    if arr[r][c] - arr[i][j] == 1:
                        visited[arr[i][j]] = 1

    cnt = 1
    result = 0
    _min = 0
    for i in range(len(visited)-1, -1, -1):
        if visited[i]:
            cnt += 1
        else:
            if result <= cnt:
                result = cnt
                _min = i + 1
            cnt = 1

    print(_min, result)









