import sys

sys.stdin = open('input (43).txt', 'r')

for tc in range(1, 11):

    n = int(input())

    arr = [list(map(str, input())) for _ in range(8)]

    result = 0

    for i in range(8):
        for j in range(8-n+1):
            for k in range(n//2):
                if arr[i][j+k] != arr[i][j+n-1-k]:
                    break
            else:
                result += 1
            for k in range(n//2):
                if arr[j+k][i] != arr[j+n-1-k][i]:
                    break
            else:
                result += 1

    print('#{}'.format(tc), end=' ')
    print(result)
















