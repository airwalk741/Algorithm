import sys
sys.stdin = open('input (43).txt', 'r')
from collections import deque

def operation(num, a):

    if a == 0:
        if num % 3:
            return num
        else:
            return num // 3
    elif a == 1:
        if num % 2:
            return num
        else:
            return num // 2
    else:
        return num - 1

def bfs(num):
    global result

    q = deque()

    q.append(num)

    while q:

        length = len(q)
        result += 1
        for _ in range(length):

            now = q.popleft()

            for i in range(3):

                next = operation(now, i)

                if -1 < next < 10 ** 6:
                    if next == 1:
                        return
                    else:
                        if visited[next] == 0:
                            q.append(next)
                            visited[next] = 1


n = int(input())

visited = [0] * (10 ** 6)

result = 0

if n == 1:
    print(result)
else:
    bfs(n)
    print(result)



