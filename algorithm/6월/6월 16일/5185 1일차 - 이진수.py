import sys
sys.stdin = open('input (43).txt', 'r')
# 10 11 12 13 14 15
hex = {
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

def binary(num):

    num = int(num)
    result = ['0'] * 4
    i = 3
    while num:

        result[i] = str(num % 2)

        num = num // 2

        i -= 1

    return ''.join(result)


T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')

    result = ''

    n, num = input().split()

    for i in range(int(n)):
        if num[i] not in hex.keys():
            result += binary(num[i])
        else:
            result += hex[num[i]]

    print(result)


