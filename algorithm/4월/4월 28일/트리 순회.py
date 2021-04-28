import sys
sys.stdin = open('input (43).txt', 'r')

def num(a):

    a = ord(a)

    return a - 64

def alph(number):

    number += 64

    return chr(number)


def preorder(idx):

    if idx != 0:
        print(alph(idx), end='')
        preorder(real_tree[idx][0])
        preorder(real_tree[idx][1])

def inorder(idx):

    if idx != 0:
        inorder(real_tree[idx][0])
        print(alph(idx), end='')
        inorder(real_tree[idx][1])

def postorder(idx):

    if idx != 0:
        postorder(real_tree[idx][0])
        postorder(real_tree[idx][1])
        print(alph(idx), end='')

n = int(input())

arr = []

for i in range(n):

    p, s1, s2 = map(num, input().split())
    arr.append((p, s1, s2))

real_tree = [[0] * 2 for _ in range(n+1)]

for tree in arr:

    if tree[1] != -18:
        real_tree[tree[0]][0] = tree[1]
    if tree[2] != -18:
        real_tree[tree[0]][1] = tree[2]



preorder(1)
print()
inorder(1)
print()
postorder(1)

