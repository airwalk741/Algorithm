import sys
sys.stdin = open('input.txt', 'r')

# 4방향 탐색
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 4방향 탐색하지 못하면 후진
def back(r, c, d):

    if d == 0:
        return (r + 1, c)
    elif d == 1:
        return (r, c - 1)
    elif d == 2:
        return (r - 1, c)
    elif d == 3:
        return (r, c + 1)


# 청소하기
def search(r, c, d):
    global result

    # 처음 들어 왔을 때
    visited[r][c] = 1
    result += 1

    while 1:

        # 4방향 탐색하기 (현재보고 있는 방향에서 시계 반대방향으로 탐색)
        for i in range(4):

            idx = d - 1 - i

            if idx < 0:
                idx += 4

            x = dr[idx] + r
            y = dc[idx] + c

            if not visited[x][y] and not arr[x][y]:
                d = idx ## 주의!!!
                break

        # 4방향 해도 청소 할 곳 없으면 후진하기
        if visited[x][y] or arr[x][y]:
            x, y = back(r, c, d) ## back(r, c, d) 주의하기
            r = x
            c = y

            if arr[x][y]: # 만약 후진했는데 벽이면 함수 나오기
                break

        # 청소할 곳 찾았을 때
        if not visited[x][y] and not arr[x][y]:
            visited[x][y] = 1
            result += 1
            r = x
            c = y



n, m = map(int, input().split())

nr, nc, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

result = 0

search(nr, nc, d)

print(result)






