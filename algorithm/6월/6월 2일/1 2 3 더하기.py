import sys
sys.stdin = open('input (43).txt', 'r')

def search(num):
    global result

    if num == n:
        result += 1
    elif num < n:
        for i in range(1, 4):
            search(num + i)


T = int(input())

for _ in range(T):

    n = int(input())

    result = 0

    search(0)

    print(result)