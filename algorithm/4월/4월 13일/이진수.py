import sys

sys.stdin = open('input (43).txt', 'r')


number = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}

def change(num):

    try:
        num = int(num)
    except:
        num = number[num]

    change_num = ''

    while len(change_num) != 4:

        change_num += str(num % 2)
        num = num // 2

    change_num = change_num[::-1]

    return change_num

T = int(input())

for tc in range(1, T+1):

    print('#{}'.format(tc), end=' ')

    n, num = input().split()

    result = ''

    n = int(n)

    for i in range(n):
        result += change(num[i])

    print(result)
