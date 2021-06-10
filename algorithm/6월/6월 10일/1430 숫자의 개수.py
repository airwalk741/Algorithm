import sys
sys.stdin = open('input (43).txt', 'r')

a = int(input())
b = int(input())
c = int(input())

cnt = [0] * 10

res = list(map(int, str(a * b * c)))

for i in range(10):
    cnt[i] = res.count(i)

for i in cnt:
    print(i)
