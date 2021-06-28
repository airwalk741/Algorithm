import sys

sys.stdin = open('input (43).txt', 'r')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bfs(R, C):

    q = [[R, C]]

    while len(q):
        num = q.pop(0)

        for i in range(4):
            x = num[0] + dr[i]
            y = num[1] + dc[i]
            if -1 < x < r and -1 < y < c: # 맵 안쪽의 인덱스인지 확인
                if arr[x][y]: # 이동할 수 있다면
                    arr[x][y] = 0 # 이동했음을 체크
                    q.append([x, y])
                    result[x][y] = result[num[0]][num[1]] + 1 # 그전까지의 거리 + 1



r, c = map(int, input().split())

# 미로
arr = [list(map(int, input())) for _ in range(r)]

# bfs로 거리
result = [[0]*c for _ in range(r)]

bfs(0, 0)

print(result[r-1][c-1] + 1)