import sys
from collections import deque
sys.stdin = open('input (43).txt', 'r')
input = sys.stdin.readline

# 토마토1과 풀이 방식 같음

dr = [-1, 0, 1, 0, 0, 0]
dc = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

n, m, h = map(int, input().split())

box = []

# 3차원 박스 만들기
for _ in range(h):
    fake_box = [list(map(int, input().split())) for _ in range(m)]
    box.append(fake_box)

tomato = deque()

# 처음에 토마토 있는 index 찾아서 tomato에 담기
for i in range(h):
    for j in range(m):
        for k in range(n):
            if box[i][j][k] == 1:
                tomato.append([i, j, k])


tomato.append([-1]) # 하루가 끝남을 -1로 알려준다.
result = 0

while tomato:

    num = tomato.popleft() # 맨앞에서부터 꺼내기

    if num[0] == -1: # -1 나오면 하루가 끝난거니까

        if len(tomato): # 뒤에 또 토마토 있으면
            result += 1 # 날짜 추가
            tomato.append([-1]) # 다음날짜임을 알려주는 것 추가
            continue
        else: # 뒤에 토마토 없으면 나가야 한다.
            break

    for i in range(6):
        x = num[1] + dr[i]
        y = num[2] + dc[i]
        z = num[0] + dz[i]

        if -1 < x < m and -1 < y < n and -1 < z < h:
            if box[z][x][y] == 0: # 토마토 안익은거가 주위에 있다면
                box[z][x][y] = 1 # 익었다고 만들어주고
                tomato.append([z, x, y])  # 추가하기

c = 0 # 안익은 상자가 있는지 확인하는 변수

for i in range(h):
    for j in range(m):
        if 0 in box[i][j]:
            print('-1')
            c = 1
            break
    if c:
        break
else:
    print(result)











