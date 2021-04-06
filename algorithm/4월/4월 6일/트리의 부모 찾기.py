import sys

sys.stdin = open('input (43).txt', 'r')


def dfs(idx):

    s = [idx]
    while len(s):

        x = s.pop()
        for i in range(len(result)):
            if result[x][i] == 1:
                result[x][i] = 0
                result[i][x] = 0
                real[i] = x

                s.append(i)

n = int(input())

result = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n - 1):
    x, y = map(int, input().split())
    result[x][y] = 1
    result[y][x] = 1

real = [0] * (n + 1)

dfs(1)

for i in range(2, len(real)):
    print(real[i])