import sys
sys.stdin = open('input (43).txt', 'r')


def find_set(x, p):

    while p[x] != x:
        x = p[x]
    return x

# 대표원소
def kruskal(n, edge):
    # 대표원소 초기화
    p = [i for i in range(n)]

    l2 = 0
    cnt = 0
    for w, u, v in edge:
        if find_set(u) != find_set(v):
            p[find_set(v)] = find_set(u)
            cnt += 1
            l2 += w
            if cnt == n - 1: # n-1 개의 간선 선택 완료
                return l2



T = int(input())

for tc in range(1, T+1):

    n = int(input())

    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())

    adj = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            adj[i][j] = (x[i]-x[j])**2 + (y[i]- y[j])**2
            adj[j][i] = adj[i][j]

    edge = []

    for i in range(n):
        for j in range(i+1, n):
            edge.append(((x[i]-x[j])**2 + (y[i]- y[j])**2), i, j)

    edge.sort()



