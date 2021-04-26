import sys
sys.stdin = open('input (43).txt', 'r')

def perm(cnt):

    # 길이가 m 이라면
    if cnt == m:
        print(*res)
        return

    # 작은숫자부터 큰 숫자
    for i in range(n):
        if arr[i] not in res: # res 리스트에 중복해서 들어가면 안된다.
            res.append(arr[i])
            perm(cnt + 1) # 길이 추가
            res.pop() # 원상복구


n, m = map(int, input().split())

arr = [i for i in range(1, n+1)]

res = []

perm(0)