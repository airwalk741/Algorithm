import sys
sys.stdin = open('input.txt', 'r')
import sys
from collections import deque


def bfs(s):

    q = deque()
    q.append(s)

    visited[s] = 1


    while q:

        s = q.popleft()

        for i in range(n + 1):
            if tree[s][i] or tree[i][s]:
                if not visited[i]:
                    visited[i] = visited[s] + tree[s][i]
                    q.append(i)





n = int(input())

tree = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(n - 1):

    s, e, w = map(int, input().split())

    tree[s][e] = w
    tree[e][s] = w


visited = [0] * (n + 1)


bfs(1)

root_max = max(visited)

idx = visited.index(root_max)

visited = [0] * (n + 1)

bfs(idx)

print(max(visited) - 1)






















