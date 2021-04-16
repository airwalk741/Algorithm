import sys
sys.stdin = open('input (43).txt', 'r')

T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc))

    num = int(input())

    arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    result = [0] * 8

    i = 0

    while i != 8:

        result[i] = num // arr[i]
        num %= arr[i]
        i += 1

    print(*result)