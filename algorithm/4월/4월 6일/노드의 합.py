import sys

sys.stdin = open('../4월 6일/input (43).txt', 'r')

T = int(input())

for tc in range(1, T+1):

    n, m, l = map(int, input().split())

    tree = [0] * (n + 1)

    for i in range(m):
        x, y = map(int, input().split())
        tree[x] = y


    if len(tree) % 2:
        tree[(n+1)//2] = tree[-1]
        for i in range(len(tree)-2, 0, -2):
            tree[i // 2] = tree[i] + tree[i - 1]
    else:
        for i in range(len(tree)-1, 0, -2):
            tree[i // 2] = tree[i] + tree[i-1]

    print('#{}'.format(tc), end=' ')
    print(tree[l])
