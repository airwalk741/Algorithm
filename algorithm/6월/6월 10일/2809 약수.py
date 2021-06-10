import sys
sys.stdin = open('input (43).txt', 'r')


n = int(input())
res = []
for i in range(1, (n + 1) // 2):
    if not n % i:
        if i in res:
            break
        res.append(i)
        if i != n // i:
            res.append(n // i)

res.sort()
print(*res)