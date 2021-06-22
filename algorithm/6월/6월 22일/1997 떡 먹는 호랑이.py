import sys
sys.stdin = open('input (43).txt', 'r')

d, k = map(int, input().split())

A = [0] * (d + 1)
B = [0] * (d + 1)

A[1] = 1
B[2] = 1

for i in range(3, d+1):
    A[i] = A[i-1] + A[i - 2]
    B[i] = B[i-1] + B[i - 2]

first = A[-1]
second = B[-1]

for i in range(1, 100001):

    num = k - first * i

    number = num / second

    if number == num // second:
        print(i)
        print(int(number))
        break


