import sys
sys.stdin = open('input (43).txt', 'r')


n, k = map(int, input().split())

for i in range(1, n+1):
    if not n % i:
        k -= 1
    if not k:
        print(i)
        break
else:
    print(0)