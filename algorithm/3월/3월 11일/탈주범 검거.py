import sys

sys.stdin = open('input (43).txt', 'r')

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 파이프 구멍 방향
def pipe(a):
    if a == 1:
        return [0, 1, 2, 3]
    elif a == 2:
        return [0, 2]
    elif a == 3:
        return [1, 3]
    elif a == 4:
        return [0, 1]
    elif a == 5:
        return [1, 2]
    elif a == 6:
        return [2, 3]
    elif a == 7:
        return [0, 3]

def bfs(r, c):
    global result

    q = []
    q.append([r, c])
    visited[r][c] = 1
    result = 1

    while len(q):
        a = l
        num = q.pop(0)
        hole = arr[num[0]][num[1]]
        cycle = pipe(hole)
        for i in cycle:
            x = num[0] + dr[i]
            y = num[1] + dc[i]
            # 구멍 방향으로 간 곳에 연결이 됐는지 확인
            if -1 < x < n and -1 < y < m and visited[x][y] == 0:
                if i == 0 and arr[x][y] in [1, 2, 5, 6]:
                    q.append([x, y])
                    visited[x][y] = visited[num[0]][num[1]] + 1
                elif i == 1 and arr[x][y] in [1, 3, 6, 7]:
                    q.append([x, y])
                    visited[x][y] = visited[num[0]][num[1]] + 1
                elif i == 2 and arr[x][y] in [1, 2, 4, 7]:
                    q.append([x, y])
                    visited[x][y] = visited[num[0]][num[1]] + 1
                elif i == 3 and arr[x][y] in [1, 3, 4, 5]:
                    q.append([x, y])
                    visited[x][y] = visited[num[0]][num[1]] + 1


T = int(input())

for tc in range(1, T+1):

    print('#{}'.format(tc), end=' ')
    n, m, r, c, l = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    visited = [ [0] * m for _ in range(n) ]

    result = 0
    bfs(r, c)

    # print(result)
    cnt = 0
    for i in range(n):
        for j in range(m):
           if visited[i][j] != 0 and visited[i][j] <= l:
               cnt += 1

    print(cnt)


