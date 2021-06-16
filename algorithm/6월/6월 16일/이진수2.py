import sys
sys.stdin = open('input (43).txt', 'r')

T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')

    num = float(input())

    result = ''
    check = 1
    while num != 0:

        num *= 2

        if len(result) == 13:
            print('overflow')
            check = 0
            break

        if num >= 1:
            result += '1'
            num -= 1
        else:
            result += '0'


    if check:
        print(result)