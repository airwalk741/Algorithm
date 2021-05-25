import sys
sys.stdin = open('input (43).txt', 'r')
input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):

    commend = input().strip()

    if commend == 'top':
        try:
            print(arr[-1])
        except:
            print(-1)
    elif commend == 'size':
        print(len(arr))
    elif commend == 'pop':
        try:
            print(arr.pop())
        except:
            print(-1)

    elif commend == 'empty':
        if len(arr):
            print(0)
        else:
            print(1)
    else:
        arr.append(commend[5:])