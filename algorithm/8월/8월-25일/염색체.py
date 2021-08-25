import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

first = [input().rstrip() for _ in range(n)]
second = [input().rstrip() for _ in range(m)]

first = set(first)
second = set(second)

result = []

for i in first:

    if i in second:
        result.append(i)


result.sort()
print(len(result))
for res in result:
    print(res)