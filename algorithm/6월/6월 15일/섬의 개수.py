import sys
sys.stdin = open('input (43).txt', 'r')

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def dfs(r, c):

    s = [(r, c)]

    visited[r][c] = 1

    while s:

        r, c = s.pop()

        for i in range(8):

            x = dr[i] + r
            y = dc[i] + c

            # 방문 안했고, 땅이면 s에 추가
            if -1 < x < h and -1 < y < w:
                if not visited[x][y]:
                    if arr[x][y]:
                        s.append((x, y))
                        visited[x][y] = 1


while True:

    w, h = map(int, input().split())

    # 0, 0 이면 끝
    if (w, h) == (0, 0):
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    result = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] and not visited[i][j]:
                result += 1
                dfs(i, j)


    print(result)
