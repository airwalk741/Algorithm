import sys
from collections import deque
sys.stdin = open('input (43).txt', 'r')

input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

tomato = deque()


m, n = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(n)]

result = 0

for i in range(n):
    for j in range(m):
        if box[i][j] == 1: # 익은 토마토 찾기
            tomato.append([i, j])

result = 0

tomato.append([-1, -1]) # 날을 판별하기 위해서 -1, -1 넣음 이거 뽑히면 다음날

while tomato:

    r, c = tomato.popleft()

    if r == -1: # 다음낳이라면
        result += 1
        if len(tomato):
            tomato.append([-1, -1]) # 다음날임을 알리기 위해 추가 (-1 나오면 다음날임)
        else: # 뒤에 더이상 없으면 끝 ( 다음날에 토마토 안익은거 없으면 끝)
            break

    else:
        for i in range(4): # 주위에 익지 않은 토마토 있으면 추가하기
            x = r + dr[i]
            y = c + dc[i]
            if -1 < x < n and -1 < y < m:
                if box[x][y] == 0:
                    box[x][y] = 1
                    tomato.append([x, y])

for i in range(n):
    if 0 in box[i]: # 중간데 안익은 토마토 있으면 -1 출력
        print('-1')
        break
else: # 그렇지 않으면 날짜 출력
    print(result - 1)
