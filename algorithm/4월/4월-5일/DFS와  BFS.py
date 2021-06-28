import sys

sys.stdin = open('input (43).txt', 'r')

# 최장거리
def dfs(idx):

    print(idx, end=' ')

    for i in range(n+1): # 1부터 시작할려고 n+1
        if arr[idx][i]: # 연결되어있다면
            if visited[i] == 0: # 방문하지 않았다면
                visited[i] = 1 # 방문체크
                dfs(i) # 연결된 방향으로 이동

# 최단거리
def bfs(idx):

    print(idx, end=' ')
    visited[idx] = 1

    q = [idx]

    while len(q):
        num = q.pop(0)

        for i in range(n+1):
            if arr[num][i]: # 연결되어 있다면
                if visited[i] == 0:
                    q.append(i)
                    print(i, end=' ')
                    visited[i] = 1


n, m, v = map(int, input().split())

arr = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1


visited = [0] * (n+1)
visited[v] = 1
dfs(v)
print()
visited = [0] * (n + 1) # 방문체크 초기화
bfs(v)
print()

