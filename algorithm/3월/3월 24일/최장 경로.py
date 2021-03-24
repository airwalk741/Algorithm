import sys

sys.stdin = open('input (43).txt', 'r')

def dfs(idx, k):
    global result

    if k > result:
        result = k

    for i in range(1, n+1):
        if arr[idx][i] and not visited[i]:
            visited[i] = 1
            dfs(i, k+1)
            visited[i] = 0


T = int(input())

for tc in range(1, 1+T):

    n, m = map(int, input().split())

    print('#{}'.format(tc), end=' ')

    arr = [[0] * (n+1) for _ in range(n+1)]

    visited = [0] * (n+1)
    visited2 = [0] * (n+1)

    for i in range(m):
        r, c = map(int, input().split())
        arr[r][c] = 1
        arr[c][r] = 1

    result = 0
    for i in range(1, n+1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0

    print(result)