import sys

sys.stdin = open('input (43).txt', 'r')

def dfs(idx, _sum):

    if _sum >= b:
        result.append(_sum)
        return

    if idx >= n:
        return

    dfs(idx+1, _sum+arr[idx])
    dfs(idx+1, _sum)

T = int(input())

for tc in range(1, T+1):

    print('#{}'.format(tc), end=' ')
    n, b = map(int, input().split())

    result = []

    arr = list(map(int, input().split()))

    dfs(0, 0)
    print(min(result)-b)