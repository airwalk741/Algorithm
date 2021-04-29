import sys
sys.stdin = open('input (43).txt', 'r')


def perm(res, idx, cnt):

    if idx == m:
        print(*res)
        return
    else:
        for i in range(cnt, n):
            if arr[i] not in res:
                res.append(arr[i])
                perm(res, idx+1, arr[i])
                res.pop()



n, m = map(int, input().split())

arr = [i for i in range(1, n+1)]

perm([], 0, 0)