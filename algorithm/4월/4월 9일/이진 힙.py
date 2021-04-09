import sys
sys.stdin = open('input (43).txt', 'r')

def hip(idx):

    if idx <= 1:
        return

    if tree[idx] < tree[idx//2]:
        tree[idx], tree[idx//2] = tree[idx//2], tree[idx]
        hip(idx//2)


T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    n = int(input())

    arr = list(map(int, input().split()))

    tree = [0]

    for i in arr:
        tree.append(i)
        hip(len(tree)-1)

    result = 0

    idx = len(tree)-1
    while True:

        if idx < 1:
            break
        result += tree[idx//2]
        idx = idx // 2

    print(result)

