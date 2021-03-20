import sys

sys.stdin = open('input (43).txt', 'r')

dr = [0, 1]
dc = [1, 0]

def dbf(r, c, count):
    global result


    count += arr[r][c]

    if visited[r][c] == 0:
        visited[r][c] = 1

    if r+1 < m:
        dbf(r+1, c, count)

    if c+1 < n:
        dbf(r, c+1, count)


    if result < count:
        result = count



n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(m)]

result = 0

visited = [[0] * n for _ in range(m)]

dbf(0, 0, 0)

print(result)

