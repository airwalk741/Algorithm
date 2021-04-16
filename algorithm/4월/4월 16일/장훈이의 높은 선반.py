import sys
sys.stdin = open('input (43).txt', 'r')

def dfs(idx, _sum, remain):
    global result


    if idx == n or _sum + remain < b or _sum >= b:
        if b <= _sum:
            result = min(result, _sum - b)
        return



    dfs(idx+1, _sum, remain-arr[idx])
    dfs(idx+1, _sum+arr[idx], remain-arr[idx])


T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')

    n, b = map(int, input().split())

    arr = list(map(int, input().split()))

    remain = sum(arr)

    result = 987654321

    dfs(0, 0, remain)

    print(result)