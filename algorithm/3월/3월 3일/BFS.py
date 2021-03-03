
def BFS(arr, value):

    visited = [0] * (n+1)
    res = []
    q = []
    q.append(value)

    while q:
        t = q.pop(0)
        if not visited[t]:
            visited[t] = 1
            res.append(t)
        for i in range(n+1):
            if arr[t][i] == 1:
                if not visited[i]:
                    q.append(i)

    return res

link = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

n = 7

arr = [[0] * (n+1) for _ in range(n+1)]

for i in range(0, len(link), 2):
    arr[link[i]][link[i+1]] = 1
    arr[link[i+1]][link[i]] = 1


print(BFS(arr, 1))