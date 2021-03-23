import sys

sys.stdin = open('input (43).txt', 'r')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def search(r, c, cnt):
    global max_count
    global result
    q = [[r, c]]

    while len(q):
        num = q.pop(0)
        for i in range(4):
            x = dr[i] + num[0]
            y = dc[i] + num[1]
            if -1 < x < n and -1 < y < n:
                if arr[num[0]][num[1]] == arr[x][y] - 1:
                    cnt += 1
                    q.append([x, y])

    if cnt > max_count:
        max_count = cnt
        result = arr[r][c]
    elif cnt == max_count:
        if result > arr[r][c]:
            result = arr[r][c]


T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    result = 987654321
    max_count = 0

    for i in range(n):
        for j in range(n):
            search(i, j, 1)

    print(result, max_count)
























