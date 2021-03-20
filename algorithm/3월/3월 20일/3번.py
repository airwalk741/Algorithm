import sys

sys.stdin = open('input (43).txt', 'r')

dr = [0, 1, 1]
dc = [1, 1, 0]

def bfs(r, c, k):
    global result
    q = []
    q.append([r, c])
    if visited[r][c] == 0:
        visited[r][c] = 1
    wei = 0
    count = 0
    while q:

        x, y = q.pop(0)

        for i in range(3):

            num1 = x + dr[i]
            num2 = y + dc[i]
            if num1 < n and num2 < n:
                if num1 >= r + k or num2 >= c + k:
                    return
                if arr[num1][num2] == 1:
                    if visited[num1][num2] == 0:
                        q.append([num1, num2])
                        visited[num1][num2] = 1

                else:
                    return

            else:
                return



n = int(input())

arr = [list(map(int, input())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

result = [0] * (n + 1)

visited2 = []
for i in range(len(visited)):
    visited2.append(list(visited[i]))

for i in range(n):
    for j in range(n):
        for v in range(2, n+1):
            bfs(i, j, v)
            _sum = 0
            for l in range(len(visited)):
                _sum += sum(visited[l])
            if _sum == (v * v):
                result[v] += 1
            for d in range(len(visited2)):
                visited[d] = list(visited2[d])
        if arr[i][j] == 1:
            result[1] += 1


print('total: {}'.format(sum(result)))

for i in range(len(result)):
    if i + 1 < len(result):
        if result[i+1] != 0:
            print('size[{}]: {}'.format(i+1, result[i+1]))

# total: 11
# size[1]: 8
# size[2]: 3