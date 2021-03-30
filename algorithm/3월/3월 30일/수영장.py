import sys

sys.stdin = open('input (43).txt', 'r')

def su(idx, total):
    global result
    global mon

    if idx >= len(mon):
        if result > total:
            result = total

        return


    su(idx+1, total + mon[idx] * rate[0])

    su(idx+1, total + rate[1])

    su(idx+3, total + rate[2])



T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    rate = list(map(int, input().split()))

    mon = list(map(int, input().split()))

    fake_mon = list(mon)

    result = rate[3]

    su(0, 0)

    print(result)