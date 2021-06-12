import sys
sys.stdin = open('input (43).txt', 'r')

n = int(input())
m = int(input())

isPrime = [1] * (m + 1)

isPrime[0], isPrime[1] = 0, 0

for i in range(2, m+1):
    if isPrime[i]:
        k = 2
        while k * i < m + 1:
            isPrime[k * i] = 0

            k += 1

primeSum = 0
primeMin = 0

for i in range(n, m+1):

    if not primeMin:
        if isPrime[i]:
            primeMin = i

    if isPrime[i]:
        primeSum += i

if primeSum and primeMin:
    print(primeSum)
    print(primeMin)
else:
    print(-1)