import sys
sys.stdin = open('input (43).txt', 'r')
import pprint

n = int(input())

arr = [[0] * n for _ in range(n)]

num = 2

arr[0][0] = 1

k = 1
i = 1
j = 0

# (n - 1, 0) ~ ( n-1, 0) 까지의 대각선까지만 구하기
while k < n:

    if k % 2:
        # 아래에서 위로 대각선
        while i > -1:

            arr[i][j] = num
            num += 1
            i -= 1
            j += 1

        # 다음 좌표
        i += 1

    else:
        # 위에서 아래로 대각선
        while j > -1:

            arr[i][j] = num
            num += 1
            i += 1
            j -= 1

        # 다음좌표
        j += 1
    k += 1

# n이 짝수인지 홀수인지에 따라 대각선 시작끝점이 다르다
if n % 2:
    k = 1
    i = n - 1
    j = 1
else:
    k = 0
    i = 1
    j = n - 1

while k < n:

    if k % 2:
        # 아래에서 위로 대각선
        while j < n:
            arr[i][j] = num
            num += 1
            i -= 1
            j += 1

        # 다음 좌표
        i += 2
        j -= 1

    else:
        # 위에서 아래 대각선
        while i < n:
            arr[i][j] = num
            num += 1
            i += 1
            j -= 1

        # 다음 좌표표
        j += 2
        i -= 1

    k += 1


for arr1 in arr:
    print(*arr1)















