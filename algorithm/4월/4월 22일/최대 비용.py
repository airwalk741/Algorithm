import sys
sys.stdin = open('input (43).txt', 'r')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def search(r, c):

    q = [(r, c)]

    while q:

        num = q.pop(0)

        for i in range(4):
            x = num[0] + dr[i]
            y = num[1] + dc[i]
            if -1 < x < n and -1 < y < n:
                cnt = 0

                if arr[x][y] > arr[num[0]][num[1]]:
                    cnt = arr[x][y] - arr[num[0]][num[1]]

                if visited[x][y] == 0:
                    visited[x][y] = visited[num[0]][num[1]] + 1 + cnt
                    q.append((x, y))



                if visited[x][y] > visited[num[0]][num[1]] + 1 + cnt:
                    visited[x][y] = visited[num[0]][num[1]] + 1 + cnt
                    q.append((x, y))

T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    result = 987654321

    visited = [[0] * n for _ in range(n)]


    search(0, 0)

    print(visited[n-1][n-1])