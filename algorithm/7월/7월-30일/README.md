# 7월 30일

## 🚩 알파벳

[![image-20210730165849757](README.assets/image-20210730165849757.png)](https://www.acmicpc.net/problem/1987)



#### 😢 FAIL

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



#### 2번째 FAIL

- `memoizion`을 이용해 풀고자 했다.
- 현재 지점을 최대 값으로 지정해 두는데  각각 `4 방향` 마다 최댓값을 정했다.
  - 포함된 알파벳이 다를 수 있기 때문에 `4방향`으로 나눠줌

```python
import sys
sys.stdin = open('input (43).txt', 'r')
from collections import deque
import pprint

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def visited_ord(n):

    return ord(n) - 65


def dfs(r, c, idx):
    global result

    for i in range(4):
        x = dr[i] + r
        y = dc[i] + c
        if -1 < x < n and -1 < y < m:

            if not alpha[arr[x][y]]:
                if visited[x][y][i] < visited[r][c][idx] + 1:
                    alpha[arr[x][y]] = 1
                    visited[x][y][i] = visited[r][c][idx] + 1
                    result = max(result, visited[x][y][i])
                    dfs(x, y, i)
                    alpha[arr[x][y]] = 0
                elif visited[x][y][i] == visited[r][c][idx] + 1:
                    alpha[arr[x][y]] = 1
                    result = max(result, visited[x][y][i])
                    dfs(x, y, i)
                    alpha[arr[x][y]] = 0


n, m = map(int, input().split())

arr = [list(map(visited_ord, input())) for _ in range(n)]

alpha = [0] * 26
alpha[arr[0][0]] = 1


result = 0

visited = [[[0] * 4 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
visited[0][0][1] = 1
visited[0][0][2] = 1
visited[0][0][3] = 1

dfs(0, 0, 0)

print(result)


```



- 아래 TC에서 막혔다..

```
20 20
YACDEFBXZJKVAXZXBSVA
BCDEFGHIJKLMNSVUTBSV
CDEFGHIJKLMNORTXUTBS
DEFGHIJKLMNOPQWZXUTW
AFGHIJKLMNOPQRSVZXWT
XGHIJKLMNOPQRSTBXZVU
WHIJKLMNOPQRSTUVWXZZ
HIJKLMNOPQRSTUVZXWZA
IJKLMNOPQRSTUVWXZZAB
JKLMNOPQRSTUVZXWZABC
TLMNOPQRSTUVWXWZABCD
QZNOPQRSTUVZXZZABCDE
ZRSPQRSTUVZXWZABCDEF
AVUXTSTUVZXWZABCDEFG
ZBWUAWXVWXWZABCDEFGH
ZRVWVUWAXZZABCDEFGHI
SRZVZVAXZZABCDEFGHIJ
TSRZSBUZZABCDEFGHIJK
QTSRTXZZABCDEFGHIJKL
CQTQQZZABCDEFGHIJKLM
```

- `OUTPUT = 26`
- 나는 25

