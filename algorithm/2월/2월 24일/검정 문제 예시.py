import sys

sys.stdin = open('input (3).txt', 'r')

T = int(input())

for tc in range(1, T + 1):

    n = int(input())

    arr = [list(input()) for _ in range(n)]


    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'A':
                for k in range(3):
                    if 0 <= i-1+k < n:
                        if arr[i - 1 + k][j] != 'B' and arr[i - 1 + k][j] != 'C':
                            arr[i - 1 + k][j] = 'x'
                    if 0 <= j - 1 + k < n:
                        if arr[i][j - 1 + k] != 'B' and arr[i][j - 1 + k] != 'C':
                            arr[i][j - 1 + k] = 'x'

            elif arr[i][j] == 'B':
                for k in range(5):
                    if 0 <= i - 2 + k < n:
                        if arr[i - 2 + k][j] != 'A' and arr[i - 2 + k][j] != 'C':
                            arr[i - 2 + k][j] = 'x'
                    if 0 <= j - 2 + k < n:
                        if arr[i][j - 2 + k] != 'A' and arr[i][j - 2 + k] != 'C':
                            arr[i][j - 2 + k] = 'x'

            elif arr[i][j] == 'C':
                for k in range(7):
                    if 0 <= i - 3 + k < n:
                        if arr[i - 3 + k][j] != 'A' and arr[i - 3 + k][j] != 'B':
                            arr[i - 3 + k][j] = 'x'
                    if 0 <= j - 3 + k < n:
                        if arr[i][j - 3 + k] != 'A' and arr[i][j - 3 + k] != 'B':
                            arr[i][j - 3 + k] = 'x'


    count = 0
    for i in range(n):
        count += arr[i].count('H')

    print(count)
