import sys

sys.stdin = open('input (6).txt', 'r')

T = int(input())

for tc in range(1, T+1):

    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    result = 0

    for i in range(n-m+1):
        for j in range(n-m+1):
            sum_arr = 0
            for x in range(i, i+m):
                for y in range(j, j+m):
                    sum_arr += arr[x][y]

            if result < sum_arr:
                result = sum_arr

    print('#{}'.format(tc), end=' ')
    print(result)












