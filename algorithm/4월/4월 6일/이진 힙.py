import sys

sys.stdin = open('../4월 6일/input (43).txt', 'r')

def left(idx):

    if idx == 1:
        # right(1)
        return
    if tree[idx] < tree[idx//2]:
        tree[idx], tree[idx//2] = tree[idx//2], tree[idx]
        left(idx//2)
#
# def right(idx):
#
#     if idx * 2 + 1 >= len(tree):
#         return
#
#     if tree[idx] > tree[idx * 2 + 1]:
#         tree[idx], tree[idx * 2 + 1] = tree[idx * 2 + 1], tree[idx]
#         right(idx * 2 + 1)


def _sum(idx):
    global result

    if idx == 0:
        return
    result += tree[idx//2]
    _sum(idx//2)

T = int(input())

for tc in range(1, 1+T):
    print('#{}'.format(tc), end=' ')

    n = int(input())

    num = list(map(int, input().split()))

    tree = [0]

    while len(num):

        tree.append(num.pop(0))
        left(len(tree)-1)

    # print(tree)
    result = 0
    _sum(len(tree)-1)
    print(result)
