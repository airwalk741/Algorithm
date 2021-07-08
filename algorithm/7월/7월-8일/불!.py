import sys
sys.stdin = open('input (43).txt', 'r')
from collections import deque
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 불 있는 곳은 지훈이가 가지 못하기 때문에
# 지훈이 이동 후 불이 퍼지는 순서대로 해야한다.
def bfs():

    cnt = 0
    # 지훈이가 이동할 수 있을 때까지 while
    while jihoon:
        cnt += 1

        jihoon_length = len(jihoon) # 담겨진 위치들 이동하기
        fire_length = len(fire) # 담겨진 위치들 퍼지기

        # 지훈이
        for _ in range(jihoon_length):

            r, c = jihoon.popleft()

            if visited[r][c] == 2: # 만약에 2라면 불이 퍼진 지점이기 때문에 패스
                continue

            # 4방향 탐색
            for i in range(4):
                x = dr[i] + r
                y = dc[i] + c
                if -1 < x < R and -1 < y < C:
                    if visited[x][y] == 0 and arr[x][y] == '.':
                        jihoon.append((x, y))
                        visited[x][y] = 1
                else:
                    # 범위 벗어나면 탈출이라고 문제에 나옴
                    return cnt

        # 불 퍼지기
        for _ in range(fire_length):

            r, c = fire.popleft()

            for i in range(4):
                x = dr[i] + r
                y = dc[i] + c
                if -1 < x < R and -1 < y < C:
                    if visited[x][y] != 2 and arr[x][y] == '.': # 불 퍼진곳 아니면 다 체크
                        fire.append((x, y))
                        visited[x][y] = 2

    # 지훈이 밖으로 피신 못했네
    return -1

R, C = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(R)]

visited = [[0] * C for _ in range(R)]

jihoon = deque() # 지훈이가 갈 수 있는 곳
fire = deque() # 불이 갈 수 있는 곳

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'J': # 지훈이 위치 담기
            jihoon.append((i, j))
            visited[i][j] = 1

        if arr[i][j] == 'F': # 불 위치 담기
            fire.append((i, j))
            visited[i][j] = 2

result = bfs()

if result == -1:
    print('IMPOSSIBLE')
else:
    print(result)



