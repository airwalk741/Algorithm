import sys
sys.stdin = open('input (43).txt', 'r')
from collections import deque

def search(s, re, visited1):

    q = deque()
    q.append(s)

    if re:
        first = 1
        second = 0
    else:
        first = 0
        second = 1

    while q:

        num = q.popleft()

        for i in range(m):

            if arr[i][first] == num:

                if visited1[arr[i][second]] > visited1[num] + arr[i][2]:
                    visited1[arr[i][second]] = visited1[num] + arr[i][2]
                    q.append(arr[i][second])


T = int(input())

for tc in range(1, T+1):

    n, m, x = map(int, input().split())

    arr = []

    for i in range(m):

        s, e, w = map(int, input().split())

        arr.append((s, e, w))


    visited1 = [987654321] * (n+1)
    visited1[x] = 0
    visited2 = [987654321] * (n+1)
    visited2[x] = 0

    search(x, 0, visited1)
    search(x, 1, visited2)


    _sum = []

    for i in range(1, n+1):
        _sum.append(visited1[i] + visited2[i])

    print('#{} {}'.format(tc, max(_sum)))


