import sys

sys.stdin = open('input (43).txt', 'r')

n, k, m = map(int, input().split())

arr = [1] * n

result = 987654321

i = -1
cnt = 0
while result != m:

    if len(arr) == 0:
        break

    i = (i + k) % len(arr)
    arr.pop(i)
    result = i + 1
    cnt += 1

print(cnt)