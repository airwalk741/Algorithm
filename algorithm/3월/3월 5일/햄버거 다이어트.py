import sys

sys.stdin = open('input (43).txt', 'r')

def burger(idx, t, k):
    global total

    if idx == n:
        if k <= l and t > total:
            total = t
        return
    if k > l:
        return

    burger(idx+1, t+taste[idx], k+kal[idx])

    burger(idx+1, t, k)


T = int(input())

for tc in range(1, T+1):

    n, l = map(int, input().split())

    taste = []
    kal = []

    for _ in range(n):
        x, y = map(int, input().split())
        taste.append(x)
        kal.append(y)
    total = 0
    burger(0, 0, 0)

    print(total)

