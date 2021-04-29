import sys
sys.stdin = open('input (43).txt', 'r')
from collections import deque
input = sys.stdin.readline

def bfs(idx):

    q = deque()

    q.append(idx)

    while q:
        num = q.popleft()
        res = 0
        while arr:

            next_num = arr.popleft()

            if next_num[0] == num:
                if visited[next_num[1]] > visited[num] + 1:
                    visited[next_num[1]] = visited[num] + 1
                    if visited[next_num[1]] <= k:
                        q.append(next_num[1])
                        res = 1

            else:
                if res:
                    break

n, m, k, x = map(int, input().split())



node = [list(map(int, input().split())) for _ in range(m)]

node.sort()

arr = deque()

arr += node


visited = [987654321] * (n+1)
visited[x] = 0

bfs(x)
res = 1

while True:

    try:
        number = visited.index(k)
        res = 0
    except:
        break

    print(number)
    visited[number] = 987654321

if res:
    print(-1)

