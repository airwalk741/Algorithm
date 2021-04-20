import sys
sys.stdin = open('input (43).txt', 'r')

def dfs(r, cnt):
    global result

    if result >= cnt:
        return

    if r == n:
        result = cnt
        return

    if cnt == 0:
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(r + 1, cnt * arr[r][i] / 100)
            visited[i] = 0


T = int(input())

for tc in range(1, 1+T):
    print('#{}'.format(tc), end=' ')
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    visited = [0] * n

    dfs(0, 1)

    print('%.6f' % (result * 100))

