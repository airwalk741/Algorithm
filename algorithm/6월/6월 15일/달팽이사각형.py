import sys
sys.stdin = open('input (43).txt', 'r')

n = int(input())

arr = [[0] * n for _ in range(n)]

i = 0 # 행
j = 0 # 열
num = 1


while True:

    colum = 0
    # 좌에서 우
    while j + colum < n:

        if not arr[i][j + colum]:
            arr[i][j + colum] = num
            num += 1
            colum += 1
        else:
            break

    i += 1
    j = j + colum - 1

    row = 0

    # 위에서 아래
    while i + row < n :

        if not arr[ i+ row][j]:
            arr[i + row][j] = num
            num += 1
            row += 1
        else:
            break

    i = i + row - 1
    j -= 1

    colum = 0

    # 우에서 좌
    while True:

        if not arr[i][j - colum]:
            arr[i][j - colum] = num
            num += 1
            colum += 1
        else:
            break

    i -= 1
    j = j - colum + 1

    row = 0

    # 아래에서 위
    while True:

        if not arr[i - row][j]:
            arr[i - row][j] = num
            num += 1
            row += 1
        else:
            break

    i = i - row + 1
    j += 1

    try:
        if arr[i][j]:
            break
    except:
        break

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()


