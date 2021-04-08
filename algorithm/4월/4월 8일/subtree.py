import sys
sys.stdin = open('input (43).txt', 'r')

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

    arr = list(map(int, input().split()))

    tree = [[0] * 2 for _ in range(e+2)]

    for i in range(0, len(arr)-1, 2):
        if tree[arr[i]][0]:
            tree[arr[i]][1] = arr[i+1]
        else:
            tree[arr[i]][0] = arr[i+1]

    cnt = 0

    inorder(n)

    print(cnt)