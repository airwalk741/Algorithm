import sys

sys.stdin = open('../4월 6일/input (43).txt', 'r')

def operation(a, b, c):
    a = int(a)
    b = int(b)
    if c == '-':
        return a-b
    elif c == '+':
        return a+b
    elif c == '/':
        return a/b
    elif c == '*':
        return a*b

for tc in range(1, 11):
    print('#{}'.format(tc), end=' ')
    n = int(input())

    tree = [0] * (n+1)

    tree_idx = [[0] * 2 for _ in range(n+1)]

    for i in range(n):
        arr = list(input().split())
        if len(arr) == 4:
            tree_idx[int(arr[0])] = [int(arr[2]), int(arr[3])]

        tree[int(arr[0])] = arr[1]

    for i in range(len(tree_idx)-1, 0, -1):
        if tree_idx[i][0]:

            # print(tree[tree_idx[i][0]], tree[tree_idx[i][1]], tree[i])
            tree[i] = operation(tree[tree_idx[i][0]], tree[tree_idx[i][1]], tree[i])


    print(int(tree[1]))











