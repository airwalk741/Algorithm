import sys

sys.stdin = open('input (43).txt', 'r')

T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')

    num = float(input())

    result = ''

    while len(result) != 14:

        if num == 0:
            break

        number = num * 2

        if number >= 1:
            result += '1'
            num = number - 1
        else:
            result += '0'
            num = number

    if len(result) > 12:
        print('overflow')
    else:
        print(result)

