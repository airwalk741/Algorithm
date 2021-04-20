import sys
sys.stdin = open('input (43).txt', 'r')

def bus(idx, cnt):
    global result

    if idx >= len(arr):
        if result >= cnt:
            result = cnt
        return

    if result <= cnt:
        return

    for i in range(idx + arr[idx], idx, -1):
        bus(i, cnt + 1)



T = int(input())

for tc in range(1, T+1):

    print('#{}'.format(tc), end=' ')
    arr = list(map(int, input().split()))

    n = arr[0]


    result = 987654321

    bus(1, 0)

    print(result-1)
