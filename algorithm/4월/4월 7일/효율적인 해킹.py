import sys
from collections import deque


def dfs(idx):
    global cnt
    global result

    s = deque()
    visited[idx] = 1
    s = [idx]

    while len(s):
        num = s.pop()
        for i in computer[num]:
            if visited[i] == 0:
                s.append(i)
                cnt += 1
                visited[i] = 1

    result[idx] = cnt # idx: 컴퓨터 번호, cnt : 해킹 할 수 있는 컴퓨터 수

n, m = map(int, input().split())

computer = [[] for _ in range(n+1)]
visited = [0] * (n+1)

com_idx = []

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    computer[y].append(x)
    com_idx.append(y)

com_idx = list(set(com_idx))

result = [0] * (n+1)

v = list(visited)

for i in com_idx:
    cnt = 0
    dfs(i)
    visited = list(v)

max_cnt = max(result)
real = []

while True:

    try:
        i = result.index(max_cnt)
        real.append(i)
        result[i] = 0

    except:
        break


print(*real)