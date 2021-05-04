# 5월 4일

## 1. 쉬운 최단 거리

#### 문제

```
지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.

문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.
```

```
지도의 크기 n과 m이 주어진다. n은 세로의 크기, m은 가로의 크기다.(2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)

다음 n개의 줄에 m개의 숫자가 주어진다. 0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다. 입력에서 2는 단 한개이다.

각 지점에서 목표지점까지의 거리를 출력한다. 원래 벽인 위치는 0을 출력하고, 원래 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.
```



#### 풀이

```python
import sys
sys.stdin = open('input (43).txt', 'r')
input = sys.stdin.readline
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 최단거리 BFS
def bfs(r, c):

    q = deque()
    q.append((r, c))
    while q:

        num = q.popleft()
        for i in range(4):
            x = num[0] + dr[i]
            y = num[1] + dc[i]
            if -1 < x < n and -1 < y < m:
                if visited[x][y] == 0 and arr[x][y] == 1:
                    visited[x][y] = visited[num[0]][num[1]] + 1
                    q.append((x, y))


def bfs2(r, c):
    pass

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]


# 시작점 찾기
for i in range(n):
    if 2 in arr[i]:
        r, c = (i, arr[i].index(2))
        break

visited = [[0] * m for _ in range(n)]

bfs(r, c)


for i in range(n):
    for j in range(m):
        # 울타리 속 가지 못했던 곳
        if arr[i][j] != 2 and arr[i][j] != 0 and visited[i][j] == 0:
            print('-1', end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
```



- `BFS`의 기본 문제
- 방문하지 않고 땅이였다면 출력을 `-1` 로 주어서 해결했다.

![image-20210504204254637](README.assets/image-20210504204254637.png)



## 2. 늑대와 양

#### 문제

```
크기가 R×C인 목장이 있고, 목장은 1×1 크기의 칸으로 나누어져 있다. 각각의 칸에는 비어있거나, 양 또는 늑대가 있다. 양은 이동하지 않고 위치를 지키고 있고, 늑대는 인접한 칸을 자유롭게 이동할 수 있다. 두 칸이 인접하다는 것은 두 칸이 변을 공유하는 경우이다.

목장에 울타리를 설치해 늑대가 양이 있는 칸으로 갈 수 없게 하려고 한다. 늑대는 울타리가 있는 칸으로는 이동할 수 없다. 울타리를 설치해보자.

```

```
첫째 줄에 목장의 크기 R, C가 주어진다.

둘째 줄부터 R개의 줄에 목장의 상태가 주어진다. '.'는 빈 칸, 'S'는 양, 'W'는 늑대이다.
```

```
늑대가 양이 있는 칸으로 갈 수 없게 할 수 있다면 첫째 줄에 1을 출력하고, 둘째 줄부터 R개의 줄에 목장의 상태를 출력한다. 울타리는 'D'로 출력한다. 울타리를 어떻게 설치해도 늑대가 양이 있는 칸으로 갈 수 있다면 첫째 줄에 0을 출력한다.
```



#### 풀이

```python
import sys
sys.stdin = open('input (43).txt', 'r')
input = sys.stdin.readline
from collections import deque
import pprint
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 양 주변에 울타리 만들기
def border(nr, nc):

    for i in range(4):
        x = nr + dr[i]
        y = nc + dc[i]
        if -1 < x < r and -1 < y < c:
            if arr[x][y] != 'W' and arr[x][y] != 'S':
                arr[x][y] = 'd'

def bfs(nr, nc):
    global check
    q = deque()
    q.append((nr, nc))
    while q:

        num = q.popleft()
        for i in range(4):
            x = num[0] + dr[i]
            y = num[1] + dc[i]
            if -1 < x < r and -1 < y < c:
                if visited[x][y] == 0:

                    if arr[x][y] == '.': # 갈 수 있으면 추가
                        visited[x][y] = 1
                        q.append((x, y))
                    elif arr[x][y] == 'd': # 울타리라면 진짜 울타리로 만들기
                        arr[x][y] = 'D'
                    elif arr[x][y] == 'S': # 양과 만나면 0
                        check = 0
                        return


r, c = map(int, input().split())

arr = [list(input()) for _ in range(r)]

# 양 주변 가짜 울타리 만들기
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'S':
            border(i, j)

check = 1
visited = [[0] * c for _ in range(r)]


# 진짜 울타리 만들기 ( 늑대 )
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'W':
            bfs(i, j)
        if check == 0:
            break
    if check == 0:
        break


if check:
    print(1)
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 'd': # 가짜 울타리라면 땅으로 바꾸기
                print('.', end='')
            else:
                print(arr[i][j], end='')
        print()
else:
    print(0)
```



- 최소 울타리를 구하는 것이 아니라 그냥 늑대랑 양이 만나면 안되는 문제
- 처음에는 출력을 한칸씩 띄어서 해서 `fail` 났었다
- 출력이 어떻게 되는지 항상 신경써서 코드를 작성하자



![image-20210504204522296](README.assets/image-20210504204522296.png)