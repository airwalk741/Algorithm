import sys

sys.stdin = open('input (43).txt', 'r')

def bfs(idx):

    q = [idx]

    while len(q):

        num = q.pop(0)

        for i in range(1, 101):
            if arr[num][i] == 1 and visited[i] == 0:
                visited[i] = visited[num] + 1
                arr[num][i] = 0
                q.append(i)

T = 10

for tc in range(1, T+1):

    print('#{}'.format(tc), end=' ')
    n, start = map(int, input().split())

    called = list(map(int, input().split()))

    arr = [[0] * 101 for _ in range(101)]


    visited = [0] * 101

    for i in range(0, n-1, 2):
        arr[called[i]][called[i+1]] = 1

    bfs(start)

    max_num = max(visited)

    for i in range(len(visited)-1, -1, -1):
        if max_num == visited[i]:
            print(i)
            break

