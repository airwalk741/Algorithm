import sys
sys.stdin = open('input (43).txt', 'r')


def dfs(idx, k):
    global result

    if result < k:
        result = k

    for i in arr[idx]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, k+1)
            visited[i] = 0

T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    n, m = map(int, input().split())

    arr = [[] for _ in range(n+1)]

    for i in range(m):
        n1, n2 = map(int, input().split())
        arr[n1].append(n2)
        arr[n2].append(n1)

    result = 0
    visited = [0] * (n + 1)
    for i in range(1, n+1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0

    print(result)