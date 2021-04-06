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


def postorder(idx):

    idx = int(idx)

    if tree_value[idx] in ['+', '-', '*', '/']:

        left = postorder(tree_node[idx][0])
        rigtht = postorder(tree_node[idx][1])
        tree_value[idx] = operation(left, rigtht, tree_value[idx])
        return tree_value[idx]

    else:
        return tree_value[idx]


for tc in range(1, 11):

    n = int(input())

    tree_value = [0] * (n+1)

    tree_node = [[0] * 2 for _ in range(n+1)]

    for i in range(n):

        arr = list(input().split())
        idx = int(arr[0])
        if len(arr) == 4:
            tree_node[idx] = [arr[2], arr[3]]

        tree_value[idx] = arr[1]

    postorder(1)

    print(int(tree_value[1]))












