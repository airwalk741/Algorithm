import sys
sys.stdin = open('input (43).txt', 'r')

def make(idx):
    global cnt

    if idx <= n:
        make(idx*2)
        tree[idx] = cnt
        cnt += 1
        make(idx * 2 + 1)


T = int(input())

for tc in range(1, T+1):

    n = int(input())

    tree = [0] * (n + 1)

    cnt = 1
    make(1)
    print('#{} {} {}'.format(tc, tree[1], tree[n//2]))