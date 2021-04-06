import sys

sys.stdin = open('../4월 6일/input (43).txt', 'r')

def make_tree(idx):
    global cnt

    if idx <= n:
        make_tree(idx * 2)
        tree[idx] = cnt
        cnt += 1
        make_tree(idx * 2 + 1)



T = int(input())

for tc in range(1, T+1):


    n = int(input())

    num = 1
    i = 1
    tree = [0] * (n + 1)

    cnt = 1
    make_tree(1)
    print('#{} {} {}'.format(tc, tree[1], tree[int(n/2)]))












