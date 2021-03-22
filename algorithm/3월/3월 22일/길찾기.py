import sys

sys.stdin = open('input (43).txt', 'r')


def dfs(idx):
    global result

    s = [idx]

    while len(s):
        num = s.pop()

        for i in range(100):
            if visited[num][i]:
                visited[num][i] = 0
                s.append(i)
        if 99 in s:
            result = 1
            return



for tc in range(1, 11):

    t, n = map(int, input().split())
    print('#{}'.format(t), end=' ')
    arr = list(map(int, input().split()))

    visited = [[0]*100 for _ in range(100)]

    result = 0

    for i in range(0, len(arr)-1, 2):
        visited[arr[i]][arr[i+1]] = 1

    dfs(0)

    print(result)