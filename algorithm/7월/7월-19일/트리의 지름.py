import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from collections import deque

## 현재 거리에서 모든 노드까지의 거리 구하기
def bfs(s):

    q = deque()
    q.append(s)

    while q:

        s = q.popleft()

        for i in range(len(tree[s])):

            e, w = tree[s][i]

            if not visited[e]:
                visited[e] = visited[s] + w
                q.append(e)



n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n - 1):

    s, e, w = map(int, input().split())

    tree[s].append((e, w))
    tree[e].append((s, w))


visited = [0] * (n + 1)


bfs(1)
# 가장 긴 거리
root_max = max(visited)

# 가장 긴 거리의 idx
idx = visited.index(root_max)

visited = [0] * (n + 1)

# 가장 긴 거이의 idx에서 실제 가장 긴 처리 찾기
bfs(idx)

print(max(visited))






















