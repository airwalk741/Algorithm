import sys
sys.stdin = open('input (43).txt', 'r')



n, k = map(int, input().split())

arr = [0] * n

for i in range(n):
    arr[i] = int(input())

result = 0

while k:

    for i in range(n):
        if arr[i] > k:
            num = k // arr[i-1]
            k = k - num * arr[i - 1]
            result += num
            break
    else:
        num = k // arr[-1]
        k = k - num * arr[-1]
        result += num

print(result)













