import sys

sys.stdin = open('input (43).txt', 'r')

def arr_sum(idx, _sum):
    global result

    if idx == n:
        if _sum == m:
            result += 1
        return

    arr_sum(idx + 1, _sum + arr[idx])
    arr_sum(idx + 1, _sum)

T = int(input())

for tc in range(1, T+1):

    n, m = map(int, input().split())

    arr = list(map(int, input().split()))


    result = 0
    print('#{}'.format(tc), end=' ')
    arr_sum(0,0)
    print(result)

