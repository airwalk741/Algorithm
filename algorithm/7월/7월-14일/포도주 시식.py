import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

n = int(input())

arr = [0] * n

for i in range(n):
    arr[i] = int(input())


dp = [0] * (n + 1)

if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0] + arr[1])
else:

    dp[1] = arr[0]
    dp[2] = arr[0] + arr[1]

    # O O X O
    # O X O
    # X
    for i in range(3, n + 1):
        dp[i] = max(dp[i-3] + arr[i - 1] + arr[i-2], dp[i-2] + arr[i - 1], dp[i-1])


    print(dp[-1])