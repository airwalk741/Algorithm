import sys
sys.stdin = open('input (43).txt', 'r')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def dfs(r, c, cnt, num):
    global result

    if cnt == 7:
        num = int(''.join(num))
        if num not in result:
            result.append(num)
        return

    for i in range(4):
        x = r + dr[i]
        y = c + dc[i]
        if -1 < x < 4 and -1 < y < 4:
            dfs(x, y, cnt+1, num+arr[x][y])



T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')

    arr = [list(input().split()) for _ in range(4)]



    result = []

    for i in range(4):
        for j in range(4):
            dfs(i, j, 1, arr[i][j])

    print(len(result))