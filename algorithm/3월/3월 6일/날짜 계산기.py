import sys

sys.stdin = open('input (43).txt', 'r')

T = int(input())

for tc in range(1, T+1):

    m1, d1, m2, d2 = map(int, input().split())

    date = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(m1):
        d1 += date[i]

    for i in range(m2):
        d2 += date[i]

    print('#{}'.format(tc), end=' ')
    print(d2-d1+1)
