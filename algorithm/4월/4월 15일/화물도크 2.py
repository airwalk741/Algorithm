import sys
sys.stdin = open('input (43).txt', 'r')

T = int(input())

for tc in range(1, 1+T):
    print('#{}'.format(tc), end=' ')
    n = int(input())

    arr = []

    for i in range(n):
        arr.append(list(map(int, input().split())))

    arr.sort(key=lambda x: x[1])

    s = arr[0][1]
    cnt = 1

    for i in range(1, n):
        if s <= arr[i][0]:
            s = arr[i][1]
            cnt += 1

    print(cnt)