import sys

sys.stdin = open('input (43).txt', 'r')

def dfs(num, r, c):

    if len(num) == 7:
        result.append(num)
        return
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for i in range(4):
        dx = r + dr[i]
        dy = c + dc[i]
        if arr[dx][dy] != 0:
            dfs(num+arr[dx][dy], dx, dy)

T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    arr = [[0] * 6]
    arr += [[0] + list(input().split()) + [0] for _ in range(4)]
    arr += [[0] * 6]
    result = []
    for i in range(1, 5):
        for j in range(1, 5):
            dfs('', i, j)

    print(len(set(result)))