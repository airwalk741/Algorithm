import sys

sys.stdin = open('input (43).txt', 'r')

def _max(idx, num):
    global result


    if idx == int(change) or idx == len(num):
        if idx == len(num):
            while idx < int(change):
                num[-1], num[-2] = num[-2], num[-1]
                idx += 1
        nun = ''
        for k in num:
            nun += str(k)
        if int(nun) > result:
            result = int(nun)

        return

    for i in range(idx, len(num)):
        for j in range(len(num)):
            if i != j:
                if num[i] <= num[j]:
                    num[i], num[j] = num[j], num[i]
                    _max(idx+1, num)
                    num[i], num[j] = num[j], num[i]

T = int(input())

for tc in range(1, T+1):

    num, change = input().split()

    number = []
    for i in num:
        number.append(int(i))

    result = 0

    _max(0, number)

    print('#{}'.format(tc), end=' ')
    print(result)