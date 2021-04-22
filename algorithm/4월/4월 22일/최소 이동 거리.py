import sys
sys.stdin = open('input (43).txt', 'r')
from collections import deque
# def dfs(r, w):
#     global result
#
#     visited[r] = 1
#
#     if w > result:
#         return
#
#     if r == N:
#         if result > w:
#             result = w
#         return
#
#     for i in range(E):
#         if arrlist[i][0] == r:
#             if visited[arrlist[i][1]] == 0:
#                 visited[arrlist[i][1]] = 1
#                 dfs(arrlist[i][1], w + arrlist[i][2])
#                 visited[arrlist[i][1]] = 0

def bfs(idx):


    q = deque()
    q.append(idx)

    while q:

        r = q.popleft()

        for i in range(E):

            if arrlist[i][0] == r:
                if visited[arrlist[i][1]] > visited[r] + arrlist[i][2]:
                    visited[arrlist[i][1]] = visited[r] + arrlist[i][2]
                    q.append(arrlist[i][1])


T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    N, E = map(int, input().split())

    arrlist = []

    for i in range(E):
        s, e, w = map(int, input().split())

        arrlist.append((s, e, w))

    arrlist.sort(key= lambda x: (x[0], -x[1], x[2]))

    result = 987654321
    visited = [987654321] * (N+1)
    visited[0] = 0

    for node in arrlist:
        if node[0] == 0:
            bfs(0)

    print(visited[N])


