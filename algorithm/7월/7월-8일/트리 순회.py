import sys
sys.stdin = open('input (43).txt', 'r')

# 전위 순회
def preorder(idx):

    print(chr(idx + 65), end='')

    if tree[idx][0]:
        preorder(ord(tree[idx][0]) - 65)
    if tree[idx][1]:
        preorder(ord(tree[idx][1]) - 65)


# 중위 순회
def inorder(idx):

    if tree[idx][0]:
        inorder(ord(tree[idx][0]) - 65)

    print(chr(idx + 65), end='')

    if tree[idx][1]:
        inorder(ord(tree[idx][1]) - 65)


# 후위 순회
def postorder(idx):

    if tree[idx][0]:
        postorder(ord(tree[idx][0]) - 65)

    if tree[idx][1]:
        postorder(ord(tree[idx][1]) - 65)

    print(chr(idx + 65), end='')


n = int(input())

tree = [[0] * 2 for _ in range(n)]

# 트리 담기
for _ in range(n):

    p, lc, rc = input().split()

    # A => 65
    p = ord(p) - 65

    if lc != '.':
        tree[p][0] = lc

    if rc != '.':
        tree[p][1] = rc


preorder(0)
print()
inorder(0)
print()
postorder(0)
