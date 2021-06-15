import sys
sys.stdin = open('input (43).txt', 'r')


n = int(input())

arr = [[-1] * n for _ in range(n)]


i = 0
j = 0
num = 0 # 숫자 0 ~ 9

while True:

    cnt = 0
    # 대각선
    while cnt + i < n and cnt + j < n:

        if arr[cnt + i][cnt + j] == -1:
            arr[cnt + i][cnt +j] = num
            num = (num + 1) % 10
            cnt += 1
        else:
            break


    j = cnt + j - 2
    i = cnt + i - 1
    cnt = 0

    # 오른쪽에서 왼쪽으로
    while True:

        if arr[i][j + cnt] == -1:
            arr[i][j + cnt] = num
            num = (num + 1) % 10
            cnt -= 1
        else:
            break

    j = j + cnt + 1
    i -= 1
    cnt = 0

    # 아래에서 위로
    while True:

        if arr[i + cnt][j] == -1:
            arr[i + cnt][j] = num
            num = (num + 1) % 10
            cnt -= 1
        else:
            break

    i = i + cnt + 2
    j = j + 1

    if arr[i][j] != -1:
        break


# 출력
for i in range(n):
    for j in range(n):
        if arr[i][j] != -1:
            print(arr[i][j], end=' ')

    print()










