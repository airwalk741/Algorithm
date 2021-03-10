import sys

sys.stdin = open('input (43).txt', 'r')


T = int(input())

for tc in range(1, 1+T):
    print('#{}'.format(tc))
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            print(arr[n-1-j][i], end='')

        print(' ', end='')

        for k in range(n):
            print(arr[n-1-i][n-1-k], end='')

        print(' ', end='')

        for q in range(n):
            print(arr[q][n-1-i], end='')

        print()