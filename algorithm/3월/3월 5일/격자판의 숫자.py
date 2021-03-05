import sys

sys.stdin = open('input (43).txt', 'r')

def number(res, r, c):


    if len(res) == 7:
        if res not in result:
            result.append(res)

        return
    else:
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        for i in range(4):

            dx = r + dr[i]
            dy = c + dc[i]

            if 0 <= dx < 4 and 0 <= dy < 4:
                number(res+arr[dx][dy], dx, dy)


T = int(input())

for tc in range(1, T+1):

    arr = [list(input().split()) for _ in range(4)]

    result = []

    for i in range(4):
        for j in range(4):
            number('', i, j)

    print('#{}'.format(tc), end=' ')
    print(len(result))

























