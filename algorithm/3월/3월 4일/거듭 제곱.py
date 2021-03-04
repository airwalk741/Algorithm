import sys

sys.stdin = open('input (43).txt', 'r')

def multi(n, m):

    if m == 0:
        return 1
    else:
        return n * multi(n, m-1)


for _ in range(10):

    tc = int(input())

    print('#{}'.format(tc), end=' ')

    n, m = map(int, input().split())

    print(multi(n, m))
