import sys
from collections import deque
sys.stdin = open('input (43).txt', 'r')
input = sys.stdin.readline
tomato = deque()

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs():
    global result

    while tomato:
        result += 1
        for _ in range(len(tomato)):
            num = tomato.popleft()
            for i in range(4):
                x = num[0] + dr[i]
                y = num[1] + dc[i]
                if -1 < x < n and -1 < y < m:
                    if box[x][y] == 0:
                        tomato.append([x, y])
                        box[x][y] = 1

    for line in box:
        if 0 in line:
            result = -1
            break


m, n = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            tomato.append([i, j])


result = 0
bfs()
print(result-1)






