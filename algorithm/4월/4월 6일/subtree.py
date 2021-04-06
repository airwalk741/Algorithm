import sys

sys.stdin = open('../4월 6일/input (43).txt', 'r')


def inorder(idx):
    global cnt
    if idx != 0:

        inorder(tree[idx][0])
        cnt += 1
        inorder(tree[idx][1])

T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')

    e, n = map(int, input().split())

    data = list(map(int, input().split()))

    tree = [[0] * 2 for _ in range(e+2)]

    cnt = 0

    for i in range(0, len(data)-1, 2):
        if tree[data[i]][0] == 0:
            tree[data[i]][0] = data[i+1]
        else:
            tree[data[i]][1] = data[i+1]

    inorder(n)

    print(cnt)

    # print(tree)