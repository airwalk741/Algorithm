import sys
sys.stdin = open('input (43).txt', 'r')
from collections import deque
input = sys.stdin.readline

# 먼저 각 빙산마다 주위에 물이 몇개 있는지 체크한다.
# 그다음 빙산 - 주위 물의 수를 하는데 이 값이 0이하가 되면 빙산의 무리를 체크한다.
# 빙산의 무리는 bfs로 체크했다.


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 빙산 주위 물의 개수 찾기
def search():
    global zero_check

    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                water[i][j] = 0
                for k in range(4):
                    x = i + dr[k]
                    y = j + dc[k]
                    if -1 < x < n and -1 < y < m:
                        if not arr[x][y]:
                            water[i][j] += 1 # 물 찾았으면 증가

    # 빙산 - 주위 물 에서 0 이하가 되는지 판별하는 변수
    zero_check = 0


# 빙산의 무리 체크하기
def bfs(r, c):

    q = deque()
    q.append((r, c))

    while q:

        r, c = q.popleft()

        for i in range(4):
            x = r + dr[i]
            y = c + dc[i]
            if -1 < x < n and -1 < y < m:
                if not visited[x][y] and arr[x][y]:
                    visited[x][y] = 1
                    q.append((x, y))


n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)] # 빙산 무리 방문체크

bingsan = 0 # 빙산의 개수 ( 빙산이 다 없어지면 0을 출력 )

for i in arr:
    bingsan += sum(i)


water = [[0] * m for _ in range(n)] # 물의 개수

result = 0

zero_check = 0 # 빙산 - 주위 물 했는데 0 이하이면 1이된다.

search()

cnt = 0 # 빙산 무리의 개수

# 처음에 빙산 무리 체크하기
for i in range(n):
    for j in range(m):
        if arr[i][j] and not visited[i][j]:
            cnt += 1
            if cnt > 1:
                break
            visited[i][j] = 1
            bfs(i, j)
    if cnt > 1:
        break

# 빙산이 남아 있고 무리가 1개일 때
while bingsan and cnt < 2:
    cnt = 0
    result += 1

    # 빙산 - 주위 물
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                if arr[i][j] <= water[i][j]:
                    bingsan -= arr[i][j]
                    arr[i][j] = 0
                    zero_check = 1
                else:
                    arr[i][j] -= water[i][j]
                    bingsan -= water[i][j]

    # 빙산이 없어졌을 때 무리 체크하기
    if zero_check:
        visited = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if arr[i][j] and not visited[i][j]:
                    cnt += 1
                    if cnt > 1:
                        break
                    visited[i][j] = 1
                    bfs(i, j)
            if cnt > 1:
                break

        # 빙산이 없어졌으니 주위 물 다시 체크

        search()

# 출력하기기
if bingsan:    print(result)
else:
    print(0)


