import sys
sys.stdin = open('input (43).txt', 'r')

def inorder(idx):

    if idx <= n:

        if len(tree[idx]) >= 3:
            inorder(int(tree[idx][2]))
        print(tree[idx][1], end='')
        if len(tree[idx]) == 4:
            inorder(int(tree[idx][3]))


for tc in range(1, 1+10):

    n = int(input())

    tree = [0] + [list(input().split()) for _ in range(n)]
    print('#{}'.format(tc), end=' ')
    inorder(1)
    print()



