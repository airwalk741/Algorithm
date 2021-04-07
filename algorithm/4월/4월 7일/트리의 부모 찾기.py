import sys
from collections import deque
sys.stdin = open('input (43).txt', 'r')


def dfs(idx):
    s = deque()
    s = [idx]

    while len(s):
        num = s.pop()
        for i in result[num]:

            result[i].remove(num)
            s.append(i)
            real[i] = num

n = int(input())

result = [[] for _ in range(n + 1)]

for i in range(n - 1):
    x, y = map(int, sys.stdin.readline().split())
    result[x].append(y)
    result[y].append(x)


real = [0] * (n + 1)

dfs(1)

for i in range(2, len(real)):
    print(real[i])