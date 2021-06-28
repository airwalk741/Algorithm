import sys

sys.stdin = open('input (43).txt', 'r')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(r, c):
    global cnt
    count = 1 # 인접한 집이 몇개 있는지 체크하는 변수

    q = [[r, c]]
    while len(q):
        num = q.pop(0)

        for i in range(4):
            x = num[0] + dr[i]
            y = num[1] + dc[i]
            if -1 < x < n and -1 < y < n:
                if arr[x][y] == 1: # 인접한 집이 있다면
                    arr[x][y] = 'x' # 방문 했음을 체크
                    count += 1
                    q.append([x, y])

    cnt.append(count) # 인접한 집 개수 추가

n = int(input())

arr = [list(map(int, input())) for _ in range(n)]

result = 0 # 인접한 집 무리 개수 담는 변수
cnt = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            result += 1 # 인접한 집 무리 개수 증가
            arr[i][j] = 'x' # 방문 체크
            bfs(i, j)

cnt.sort()
print(result)
for i in cnt:
    print(i)
