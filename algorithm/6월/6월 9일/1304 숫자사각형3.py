import sys
sys.stdin = open('input (43).txt', 'r')

n = int(input())


for i in range(n):
    for j in range(n):
        print(n*j+1 + i, end=' ')

    print()
