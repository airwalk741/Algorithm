import sys
sys.stdin = open('input (43).txt', 'r')
input = sys.stdin.readline
from collections import deque
import pprint
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 양 주변에 울타리 만들기
def border(nr, nc):

    for i in range(4):
        x = nr + dr[i]
        y = nc + dc[i]
        if -1 < x < r and -1 < y < c:
            if arr[x][y] != 'W' and arr[x][y] != 'S':
                arr[x][y] = 'd'

def bfs(nr, nc):
    global check
    q = deque()
    q.append((nr, nc))
    while q:

        num = q.popleft()
        for i in range(4):
            x = num[0] + dr[i]
            y = num[1] + dc[i]
            if -1 < x < r and -1 < y < c:
                if visited[x][y] == 0:

                    if arr[x][y] == '.': # 갈 수 있으면 추가
                        visited[x][y] = 1
                        q.append((x, y))
                    elif arr[x][y] == 'd': # 울타리라면 진짜 울타리로 만들기
                        arr[x][y] = 'D'
                    elif arr[x][y] == 'S': # 양과 만나면 0
                        check = 0
                        return


r, c = map(int, input().split())

arr = [list(input()) for _ in range(r)]

# 양 주변 가짜 울타리 만들기
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'S':
            border(i, j)

check = 1
visited = [[0] * c for _ in range(r)]


# 진짜 울타리 만들기 ( 늑대 )
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'W':
            bfs(i, j)
        if check == 0:
            break
    if check == 0:
        break


if check:
    print(1)
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 'd': # 가짜 울타리라면 땅으로 바꾸기
                print('.', end='')
            else:
                print(arr[i][j], end='')
        print()
else:
    print(0)









