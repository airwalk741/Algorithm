import sys

sys.stdin = open('input (43).txt', 'r')


def bfs(idx):
    global cnt

    visited[idx] = 1
    q = [idx]

    while len(q):
        num = q.pop(0)

        for i in range(n+1):
            if computer[num][i]:
                if visited[i] == 0:
                    visited[i] = 1
                    q.append(i)
                    cnt += 1

n = int(input())

link = int(input())

computer = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

cnt = 0

for i in range(link):
    x, y = map(int, input().split())
    computer[x][y] = 1
    computer[y][x] = 1

bfs(1)

print(cnt)