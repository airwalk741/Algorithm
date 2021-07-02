import sys
sys.stdin = open('input (43).txt', 'r')

def serach(idx, res, cnt):

    if cnt == m:
        print(res)
    else:
        for i in range(idx, n):

            serach(i, res + arr[i] + ' ', cnt + 1)




n, m = map(int, input().split())

arr = [str(i) for i in range(1, n + 1)]

serach(0, '', 0)



