import sys
sys.stdin = open('input (43).txt', 'r')

def pascal():

    for i in range(n):
        for j in range(i + 1):
            if i == j:
                arr[i][j] = 1
                break
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i - 1][j]


def first():

    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                print(arr[i][j], end=' ')
        print()


def second():

    cnt = 0
    for i in range(n-1, -1, -1):
        print(end=' '* cnt)
        for j in range(n):
            if arr[i][j]:
                print(arr[i][j], end=' ')
        cnt += 1
        print()


def third():

    for j in range(n-1, -1, -1):
        for i in range(n-1, -1, -1):
            if arr[i][j]:
                print(arr[i][j], end=' ')
        print()


n, m = map(int, input().split())

arr = [[0] * n for _ in range(n)]

pascal()

if m == 1:
    first()
elif m == 2:
    second()
else:
    third()


















