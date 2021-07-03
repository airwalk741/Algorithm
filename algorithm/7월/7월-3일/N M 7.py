import sys
sys.stdin = open('input (43).txt', 'r')

def search(res, cnt):

    if cnt == m:
        print(res)
    else:
        for i in range(n):

            search(res + arr[i] + ' ', cnt + 1)


n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

arr = list(map(str, arr))

search('', 0)