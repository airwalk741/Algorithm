import sys
sys.stdin = open('input (43).txt', 'r')



n, m = map(int, input().split())

for i in range(n):
    if i % 2:
        for j in range((i+1)*m, i*m, -1):
            print(j, end=' ')
    else:
        for j in range(i*m+1, (i+1)*m+1):
            print(j, end=' ')
    print()