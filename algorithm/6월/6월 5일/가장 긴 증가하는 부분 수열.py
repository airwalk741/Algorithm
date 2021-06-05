import sys
sys.stdin = open('input (43).txt', 'r')
input = sys.stdin.readline



n = int(input())

arr = list(map(int, input().split()))

perm = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            perm[i] = max(perm[i], perm[j] + 1)

print(max(perm))





