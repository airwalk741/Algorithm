# 7월 30일

## 🚩 알파벳

[![image-20210730165849757](README.assets/image-20210730165849757.png)](https://www.acmicpc.net/problem/1987)



#### ✍ 풀이

- `BFS` 를 이용해 거리를 구했다.
- 하지만 시간 초과
- 그래서 `DFS`를 이용해 최장 거리를 구했다.
- 하지만 시간 초과.. 다른 방법을 생각해야한다.....

```python
import sys
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def visited_ord(n):

    return ord(n) - 65


def dfs(r, c, cnt):
    global result

    for i in range(4):
        x = dr[i] + r
        y = dc[i] + c
        if -1 < x < n and -1 < y < m:
            if not visited[arr[x][y]]:
                visited[arr[x][y]] = 1
                dfs(x, y, cnt + 1)
                visited[arr[x][y]] = 0


    result = max(result, cnt)


n, m = map(int, input().split())


arr = [list(map(visited_ord, input())) for _ in range(n)]

visited = [0] * 26

result = 0
visited[arr[0][0]] = 1

dfs(0, 0, 1)

print(result)

```

