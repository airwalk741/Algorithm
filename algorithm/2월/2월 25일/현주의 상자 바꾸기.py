import sys
sys.stdin = open('input (9).txt', 'r')


T = int(input())

for tc in range(1, T + 1):

    n, q = map(int, input().split())

    arr = [0] * (n + 1)

    for i in range(1, q+1):
        l, r = map(int, input().split())

        for j in range(l, r+1):
            arr[j] = i
    print('#{}'.format(tc), end=' ')
    for i in range(1, len(arr)):
        print(arr[i], end=' ')
    print()
