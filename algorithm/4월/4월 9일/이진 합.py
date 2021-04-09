import sys
sys.stdin = open('input (43).txt', 'r')

def search(idx):

    if idx <= n:

        if tree[idx]:
            return tree[idx]
        left = idx * 2
        right = idx * 2 + 1

        return search(left) + search(right)
    return 0


T = int(input())

for tc in range(1, T+1):

    n, m, l = map(int, input().split())

    tree = [0] * (n+1)

    for i in range(m):
        x, y = map(int, input().split())
        tree[x] = y


    print(search(l))