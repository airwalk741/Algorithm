import sys
sys.stdin = open('input (43).txt', 'r')

n = int(input())

arr = [[0] * (n * 2 - 1) for _ in range(n * 2 - 1)]

n = n * 2 - 1

i = 0
j = n // 2
num = 0
ch = 0
first = 0
# A = 65, Z = 90

while not ch:

    row = 0
    column = 0

    # 2사분면 대각선 (위에서 아래로 내려가기 때문에 row 기준)
    while i + row < n // 2 + 1:

        arr[i + row][j + column] = chr((num % 26) + 65)
        row += 1
        column -= 1
        num += 1

    i = i + row
    j = j + column + 2
    row = 0
    column = 0

    # 3사분면 대각선 (좌에서 우로 가기 때문에 column 기준)
    while j + column < n // 2 + 1:

        arr[i + row][j + column] = chr((num % 26) + 65)
        row += 1
        column += 1
        num += 1


    i = i + row - 2
    j = j + column
    row = 0
    column = 0

    # 4사분면 대각선 (위에서 아래로 올라가기 때문에 row 기준)
    while i + row >= n // 2:

        arr[i + row][j + column] = chr((num % 26) + 65)
        row -= 1
        column += 1
        num += 1

    i = i + row
    j = j + column - 2
    row = 0
    column = 0

    # 1사분면 대각선 (우에서 좌로 가기 때문에 column 기준)
    while j + column > n // 2:

        arr[i + row][j + column] = chr((num % 26) + 65)
        row -= 1
        column -= 1
        num += 1

    i = i + row + 1
    j = j + column

    if arr[i][j]:
        ch = 1
        break


for i in range(n):
    for j in range(n):
        if arr[i][j]:
            print(arr[i][j], end=' ')
        else:
            print(end='  ')
    print()

























