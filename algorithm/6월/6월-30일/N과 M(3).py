import sys
sys.stdin = open('input (43).txt', 'r')

def solution(res, cnt):
    global result

    if cnt == m:
        print(res)

    else:
        for i in range(n):
            if len(res):
                solution(res + ' ' + nums[i], cnt + 1)
            else:
                solution(res + nums[i], cnt + 1)



n, m = map(int, input().split())

nums = [str(i) for i in range(1, n+1)]

result = []

solution('', 0)

