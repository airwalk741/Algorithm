import sys

sys.stdin = open('input (9).txt', 'r')

T = int(input())

for tc in range(1, T + 1):

    print('#{}'.format(tc), end=' ')
    n = int(input())

    arr = [list(map(int, input())) for _ in range(n)]

    result = 0

    # 반절에서 윗부분
    for i in range(n // 2):
        for j in range(n // 2 - i, n // 2 + 1 + i):
            result += arr[i][j]

    # 반절
    for i in range(n):
        result += arr[n // 2][i]

    # 반절에서 아랫부분
    k = 1
    for i in range(n // 2 + 1, n):

        for j in range(k, n - k):
            result += arr[i][j]

        k += 1

    print(result)
