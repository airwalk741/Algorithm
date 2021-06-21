import sys
sys.stdin = open('input (43).txt', 'r')


arr = [[0] * 100 for _ in range(100)]

result = 0

n = int(input())

for _ in range(n):

    r, c = map(int, input().split())

    for i in range(c, c + 10):
        for j in range(r, r + 10):
            arr[i][j] = 1

for i in arr:
    result += sum(i)

print(result)