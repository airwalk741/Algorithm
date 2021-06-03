import sys
sys.stdin = open('input (43).txt', 'r')


n = int(input())

arr = [0] * 300

for i in range(n):
    arr[i] = int(input())

res = [0] * 300

res[0] = arr[0]
res[1] = arr[1] + arr[0]
res[2] = max(arr[0] + arr[2], arr[1] + arr[2])

for i in range(3, n):
    res[i] = max(res[i-2] + arr[i], res[i-3] + arr[i] + arr[i-1])


print(res[n-1])











