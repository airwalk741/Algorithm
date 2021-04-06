import sys

sys.stdin = open('input (43).txt', 'r')

def bfs(idx):


    visited[idx] = 1
    q = [idx]
    print(idx, end=' ')
    while len(q):
        num = q.pop(0)

        for i in range(n+1):
            if arr[num][i]:
                if visited[i] == 0:
                    visited[i] = 1
                    q.append(i)
                    print(i, end=' ')

def dfs(idx):

    print(idx, end=' ')
    visited[idx] = 1

    for i in range(n+1):
        if arr[idx][i]:
            if visited[i] == 0:
                visited[i] = 1
                dfs(i)

    # visited[idx] = 1
    # s = [idx]
    # print(idx, end=' ')
    # while len(s):
    #     num = s.pop()
    #
    #     for i in range(n + 1):
    #         if arr[num][i]:
    #             if visited[i] == 0:
    #                 visited[i] = 1
    #                 s.append(i)
    #                 print(i, end=' ')


n, m, v = map(int, input().split())

arr = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())

    arr[x][y] = 1
    arr[y][x] = 1


visited = [0] * (n+1)
dfs(v)
print()
visited = [0] * (n+1)
bfs(v)