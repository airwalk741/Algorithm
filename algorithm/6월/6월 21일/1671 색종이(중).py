import sys
sys.stdin = open('input (43).txt', 'r')
import pprint

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

arr = [[0] * 100 for _ in range(100)]
result = 0

n = int(input())

for _ in range(n):

    r, c = map(int, input().split())

    for i in range(r, r + 10):
        for j in range(c, c + 10):
            arr[i][j] = 1

for i in range(100):
    for j in range(100):
        if arr[i][j]:
            cnt = 0
            for k in range(4):
                x = i + dr[k]
                y = j + dc[k]
                if -1 < x < 100 and -1 < y < 100:
                    if arr[x][y]:
                        cnt += 1
            if cnt == 2:
                result += 2
            elif cnt == 3:
                result += 1

print(result)

