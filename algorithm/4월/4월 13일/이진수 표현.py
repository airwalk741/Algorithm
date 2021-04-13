import sys

sys.stdin = open('input (43).txt', 'r')

num_dic = {
    '211'
}

T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')

    n, m = map(int, input().split())

    number = ''

    while len(number) != n:

        number += str(m % 2)
        m = m // 2

    if len(number) == 0:
        print('OFF')
    else:

        if '0' in number:
            print('OFF')
        else:
            print('ON')











