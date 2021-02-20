import sys

sys.stdin = open('input (6).txt', 'r')

for tc in range(1, 11):

    t = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_cross = 0
    sum_re_cross = 0
    result = 0

    for i in range(100):
        sum_row = 0
        sum_col = 0
        for j in range(100):
            sum_row += arr[i][j] # 가로 합
            sum_col += arr[j][i] # 세로 합
            if i == j:
                sum_cross += arr[i][j] # 대각선 합
            if i + j == 99:
                sum_re_cross += arr[i][j] # 반대 대각선 합

        # 합들 중에서 최댓값 구하는 if문
        if sum_row > sum_col:
            if sum_row > result:
                result = sum_row
        else:
            if sum_col > result:
                result = sum_col

    # 대각선, 반대대각선, 그 정에 구했던 가장 큰 합들 중에서 가장 큰 값 구하는 if문
    if sum_cross > sum_re_cross:
        if sum_cross > result:
            result = sum_cross
    else:
        if sum_re_cross > result:
            result = sum_re_cross
    print('#{}'.format(t), end=' ')
    print(result)
