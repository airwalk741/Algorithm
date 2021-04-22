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
    print('#{}'.format(tc), end=' ')

    n, m = map(int, input().split())
    num = list(map(int, input().split()))

    arr = [i for i in range(n+1)]

    for i in range(0, m*2, 2):
        union(num[i], num[i+1])

    result = []

    for i in range(1, len(arr)):
        result.append(find_set(arr[i]))

    print(result)
    print(arr)
    print(len(set(result)))




# [0, 1, 1, 3, 3, 5]
# [0, 1, 1, 1, 4, 4]
# [0, 1, 2, 2, 7, 4, 4, 7]