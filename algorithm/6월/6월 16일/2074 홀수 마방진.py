import sys
sys.stdin = open('input (43).txt', 'r')
import pprint

n = int(input())

arr = [[0] * n for _ in range(n)]

num = 1

# 처음 1등록
i = 0
j = n // 2
arr[i][j] = num

while num < n * n:

    # n의 배수이면 아래도 이동
    if not num % n:

        num += 1

        i += 1
        arr[i][j] = num

    # n의 배수가 아니면
    else:

        # 왼쪽 위로 이동
        num += 1

        i -= 1
        j -= 1

        # 행을 벗어나면 마지막 행으로 이동
        if i < 0:
            i = n - 1
            arr[i][j] = num
            continue

        # 열을 벗어나면 마지막 열로 이동동
        if j < 0:
           j = n - 1
           arr[i][j] = num
           continue

        arr[i][j] = num


for res in arr:
    print(*res)