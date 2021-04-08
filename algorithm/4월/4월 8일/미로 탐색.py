import sys
sys.stdin = open('input (43).txt', 'r')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(r, c): # 중심에서 퍼져나가기

    visited[r][c] = 1
    arr[r][c] = 0
    q = [[r, c]]
    while len(q):
        num = q.pop(0)

        for i in range(4):
            x = num[0] + dr[i]
            y = num[1] + dc[i]
            if -1 < x < n and -1 < y < m:
                if arr[x][y]:
                    visited[x][y] = visited[num[0]][num[1]] + 1 # 그 전까지의 길이 + 1
                    q.append([x, y])
                    arr[x][y] = 0



n, m = map(int, input().split())

arr = [ list(map(int, input())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]


bfs(0, 0)

print(visited[n-1][m-1])