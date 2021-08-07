import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

## 처음에 구석인 좌표들만 second에 담는다
## second에 담아진 좌표들 하나씩 꺼내어 최대 길이를 구해서 result 변수에 담는다.

def bfs(r, c, second_check):  ## second_check는 함수 재사용하기 위한 변수 (1일 때 구석 좌표 구하기, 0일 때는 구하지 않기)
    global result

    q = deque()
    q.append((r, c, 0))
    second.append((r, c))
    _max = 0
    visited[r][c] = 1
    while q:

        r, c, cnt = q.popleft()

        if _max < cnt:
            _max = cnt


        check = 1

        for i in range(4):
            x = r + dr[i]
            y = c + dc[i]

            if -1 < x < n and -1 < y < m:
                if not visited[x][y]:
                    if arr[x][y] == 'L':
                        visited[x][y] = 1
                        q.append((x, y, cnt + 1))
                        check = 0 ## 다음 좌표 추가되면 구석이 아니다

        if second_check:
            if check:
                second.append((r, c))

    result.append(_max) # 최대 길이 담아두기


n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]


visited = [[0] * m for _ in range(n)]

result = []

second = deque()

## 구석 좌표구하기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            if not visited[i][j]:
                bfs(i, j, 1)


## 구석 좌표들에서 최대 길이 구하기
length = len(second)
for _ in range(length):

    r, c = second.popleft()

    visited = [[0] * m for _ in range(n)]

    bfs(r, c, 0)


print(max(result))

