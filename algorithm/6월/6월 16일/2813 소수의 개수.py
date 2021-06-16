import sys
sys.stdin = open('input (43).txt', 'r')

n, m = map(int, input().split())

isPrime = [1] * (m + 1)

isPrime[0] = 0
isPrime[1] = 0
cnt = 0

for i in range(2, m + 1):
    if isPrime[i]:

        if i >= n:
            cnt += 1

        for j in range(i * i, m + 1, i):
            isPrime[j] = 0

print(cnt)