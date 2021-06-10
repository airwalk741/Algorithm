import sys
sys.stdin = open('input (43).txt', 'r')

n = int(input())

arr = list(map(int, input().split()))

target = int(input())

res1 = 0
res2 = 0

for i in range(n):

    if not arr[i] % target:
        res2 += arr[i]

    if not target % arr[i]:
        res1 += arr[i]


print(res1)
print(res2)
