import sys
sys.stdin = open('input (43).txt', 'r')

def search(r, _sum):
    global  result

    if _sum > result:
        return

    if r == n:
        if _sum < result:
            result = _sum
        return


    for j in range(n):

        if visited[j] == 0:
            visited[j] = 1
            search(r + 1, _sum + arr[r][j])
            visited[j] = 0



T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    visited = [0] * n

    result = 98765431

    search(0, 0)

    print(result)