import sys
sys.stdin = open('input (43).txt', 'r')

def dfs(idx, cnt, money):
    global result

    if cnt == n-1:
        money += cart[idx][0]
        result = min(result, money)

        return

    if result <= money:
        return

    for i in range(1, n):

        if visited[i] == 0:
            visited[i] = 1
            dfs(i, cnt + 1, money + cart[idx][i])
            visited[i] = 0


T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')

    n = int(input())

    cart = [list(map(int, input().split())) for _ in range(n)]
    result = 987654321
    visited = [0] * n

    dfs(0, 0, 0)

    print(result)