import sys
sys.stdin = open('input (43).txt', 'r')

def find_set(x):

    if x == arr[x]:
        return x
    else:
        return find_set(arr[x])

def union(x, y):

    arr[find_set(y)] = find_set(x)


T = int(input())

for tc in range(1, T+1):

    n, m = map(int, input().split())

    arr = [i for i in range(n+1)]

    for _ in range(m):
        x, y = map(int, input().split())
        union(x, y)

    cnt = 0

    for i in range(n+1):
        if i == arr[i]:
           cnt += 1

    print('#{} {}'.format(tc, cnt-1))










