import sys
sys.stdin = open('input (43).txt', 'r')
# import pprint
from collections import deque
input = sys.stdin.readline

horse_r = [-2, -1, 1, 2, 2, 1, -1, -2]
horse_c = [1, 2, 2, 1, -1, -2, -2, -1]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]



def bfs(a, b):
    global jump

    q = deque()
    q.append((a, b, jump, 0))

    while q:
        r, c, k, length = q.popleft()


        if k != 0:
            for i in range(8):

                x = r + horse_r[i]
                y = c + horse_c[i]
                if -1 < x < h and -1 < y < w and not arr[x][y]:
                    if 2 not in visited[x][y]:
                        if (x, y) == (h-1, w-1):
                            return length + 1
                        q.append((x, y, k-1, length + 1))
                        visited[x][y].append(2)


        for i in range(4):

            x = r + dr[i]
            y = c + dc[i]
            if -1 < x < h and -1 < y < w and not arr[x][y]:

                if k == 0:
                    if 3 not in visited[x][y]:
                        if (x, y) == (h - 1, w - 1):
                            return length + 1

                        visited[x][y].append(3)
                        q.append((x, y, k, length + 1))
                else:
                    if 1 not in visited[x][y]:

                        if (x, y) == (h - 1, w - 1):
                            return length + 1

                        visited[x][y].append(1)
                        q.append((x, y, k, length + 1))


    return -1


jump = int(input())

w, h = map(int, input().split())


arr = [list(map(int, input().split())) for _ in range(h)]

visited = [[[] for _ in range(w)] for _ in range(h)]
visited[0][0].append(1)
visited[0][0].append(2)

print(bfs(0, 0))

print(visited)

# [[[1,2],   [1],     [1, 2],  [1],     [1]],
# [[1],    [1],     [2, 1],  [1, 2],  [1]],
# [[1, 2], [2, 1],  [1, 2],  [1],     [1]],
# [[1],    [1, 2],  [1],     [],      []],
# [[1],    [1],     [1],     [],      []]]

#
#  [[1, 2], [1],    [1, 2], [1],    [1]],
#  [[1],    [1],    [2, 1], [1, 2], [1]],
#  [[1, 2], [2, 1], [1, 2], [1],    [1]],
#  [[1],    [1, 2], [1],    [],     []],
#  [[1],    [1],    [1],    [],     []]

# [[[1, 2], [1, 2], [], [],         [],         [],         [], []],
# [[],     [],      [], [2, 1, 3],  [1, 2, 3],  [1, 3],     [], []],
# [[],     [],      [], [],         [],         [2, 1, 3],  [], []],
# [[3],    [2, 3],  [], [],         [],         [1, 2, 3],  [], []],
# [[3],    [],      [], [3, 2, 1],  [2, 3, 1],  [3, 1],     [], []],
# [[3],    [],      [], [],         [],         [],         [], []],
# [[],     [],      [], [],         [],         [],         [], []],
# [[],     [],      [], [],         [],         [],         [], []]]
