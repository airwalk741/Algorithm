import sys

sys.stdin = open('../4월 6일/input (43).txt', 'r')

def search(idx):

    if idx >= n + 1:
        return 0
    if tree[idx]:
        return tree[idx]
    left = idx * 2
    right = left + 1
    result = search(left) + search(right)
    return result


T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    n, m, l = map(int, input().split())

    tree = [0] * (n + 1)

    for i in range(m):
        x, y = map(int, input().split())
        tree[x] = y

    result = search(l)
    print(result)