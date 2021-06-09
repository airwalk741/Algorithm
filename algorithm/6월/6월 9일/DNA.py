import sys
sys.stdin = open('input (43).txt', 'r')
input = sys.stdin.readline


n, m = map(int, input().split())

dna = [list(input()) for _ in range(n)]

result = ''
res = 0
for i in range(m):
    check = [0] * (90 - 65)
    for j in range(n):
        check[ord(dna[j][i])-65] += 1

    _max = max(check)


    res += n - _max

    result += chr(check.index(_max) + 65)

print(result)
print(res)
# A = 65
# Z = 90
