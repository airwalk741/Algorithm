import sys
sys.stdin = open('input (43).txt', 'r')
from collections import deque


# 8방향
dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(r, c):

    q = deque()

    q.append((r, c))
    cnt = -1

    while q:

        length = len(q)
        cnt += 1

        for _ in range(length):

            r, c = q.popleft()
            # 타겟 위치라면
            if (r, c) == (target_r, target_c):
                return cnt

            # 8방향 탐색
            for i in range(8):

                x = dr[i] + r
                y = dc[i] + c
                if -1 < x < n and -1 < y < n:
                    if not arr[x][y]:
                        arr[x][y] = 1 # 방문체크크
                       q.append((x, y))


T = int(input())

for _ in range(T):


    n = int(input())

    arr = [[0] * n for _ in range(n)]

    now_r, now_c = map(int, input().split())

    target_r, target_c = map(int, input().split())

    print(bfs(now_r, now_c))