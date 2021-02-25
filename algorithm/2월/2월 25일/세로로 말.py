import sys
sys.stdin = open('input (9).txt', 'r')


T = int(input())

for tc in range(1, T + 1):

    print('#{}'.format(tc), end=' ')
    arr = [list(input()) for _ in range(5)]

    arr_max = 0

    for i in range(5):
        if arr_max < len(arr[i]):
            arr_max = len(arr[i])

    for i in range(arr_max):
        for j in range(5):
            if len(arr[j]):
                print(arr[j].pop(0), end='')

    print()