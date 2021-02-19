import sys

sys.stdin = open('input (7).txt', 'r')

T = int(input())

for tc in range(1, T+1):

    n = int(input())

    arr = [list(map(int, input())) for _ in range(n)]


    result = 0

    # 위쪽 부분 더하는 것
    for i in range(n//2):
        # 중간 지점 찾아서 왼쪽
        for j in range(n//2 - i, n//2 + i +1):
            result += arr[i][j]

    # 중간부분 더하는 것
    for i in range(n):
        result += arr[n//2][i]

    # 밑 부분 더하는 것
    k = 1
    for i in range(n//2+1, n):
        # 중간지점 찾아서 양쪽으로 줄어들게 끔
        for j in range(i-(n//2), n-k):
            result += arr[i][j]
        k += 1

    print('#{}'.format(tc), end=' ')
    print(result)





