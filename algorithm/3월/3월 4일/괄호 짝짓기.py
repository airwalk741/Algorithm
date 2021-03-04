import sys

sys.stdin = open('input (43).txt', 'r')

for tc in range(1, 11):
    print('#{}'.format(tc), end=' ')
    n = int(input())

    arr = list(input())

    res = 1

    com = {
        '{': 0,
        '(': 0,
        '[': 0,
        '<': 0,
    }

    re_com = {
        '}': '{',
        '>': '<',
        ']': '[',
        ')': '('
    }

    while len(arr):

        value = arr.pop(0)

        if value in com.keys():
            com[value] += 1
        else:
            if com[re_com[value]] <= 0:
                res = 0
                break
            else:
                com[re_com[value]] -= 1

    print(res)











