import sys
sys.stdin = open('input (43).txt', 'r')

n, m = map(int, input().split())

i = max(n, m)

while True:

    if not n % i:
        if not m % i:
            break

    i -= 1

print(i)
print(n * (m // i))