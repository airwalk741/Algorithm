import sys
sys.stdin = open('input (43).txt', 'r')
from collections import deque

def operation(num, operater):

    if operater == 0:
        return num + 1
    elif operater == 1:
        return num - 1
    elif operater == 2:
        return num * 2
    elif operater == 3:
        return num - 10

def bfs(a):
    global result

    q = deque()
    q.append((a, 0))
    visited[a] = 1
    while q:

        num, cnt = q.popleft()

        for i in range(4):

            number = operation(num, i)

            if num == m:
                result = cnt
                return

            if number < 1 or number > 1000000: # m의 최대값 넘어가면 안됨
                continue

            if visited[number] == 0: # 방문체크 확인
                visited[number] = 1
                q.append((number, cnt + 1))


T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    n, m = map(int, input().split())

    visited = [0] * 10000001
    result = 0

    bfs(n)

    print(result)

















