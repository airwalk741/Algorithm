import sys
sys.stdin = open('input (43).txt', 'r')

def dfs(r, c, num):
    global result

    if r == n-1 and c == n-1: # 좌표가 오른쪽 맨 아래 가리키면 최솟값 비교
        if num < result:
            result = num
        return

    if num >= result: # 백트레킹 ( 이제까지 더한게 result보다 크면 굳이 더 구할 필요 X)
        return

    if r+1 < n: # 아래쪽으로 이동
        dfs(r+1, c, num+arr[r+1][c])
    if c+1 < n: # 오른쪽으로 이동
        dfs(r, c+1, num+arr[r][c+1])


T = int(input())

for tc in range(1, 1+T):
    print('#{}'.format(tc), end=' ')
    n = int(input())

    arr = [list(map(int,input().split())) for _ in range(n)]

    result = 987654321

    dfs(0, 0, arr[0][0])

    print(result)