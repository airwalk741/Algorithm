# 4월 8일

#### 1. 토마토

- 함수를 자꾸 호출하게 되면 시간초과함을 오늘 알았다.
- 괜히 가독성을 위해 함수를 만들어 호출 해줬었는데 설마하면서 다시 코드를 구현 해보니 `PASS`가 나왔다.
- **수정전**

```python

import sys
from collections import deque
sys.stdin = open('input (43).txt', 'r')

input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

tomato = deque()

def bfs(r, c):
    global tomato

    for i in range(4):
        x = r + dr[i]
        y = c + dc[i]
        if -1 < x < n and -1 < y < m:
            if box[x][y] == 0:
                box[x][y] = 1
                tomato.append([x, y])

m, n = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(n)]

result = 0

for i in range(n):
    for j in range(m):
        if box[i][j] == 1 and [i, j] not in tomato:
            bfs(i, j)
if tomato:
    result = 1
else:
    result = 0

tomato.append([-1, -1]) # 날을 판별하기 위해서 -1, -1 넣음 이거 뽑히면 다음날

while tomato:

    r, c = tomato.popleft()

    if r == -1: # 다음낳이라면
        result += 1
        if len(tomato):
            tomato.append([-1, -1]) # 다음날임을 알리기 위해 추가
        else: # 뒤에 더이상 없으면 끝
            break

    else: 
        bfs(r, c) 

for i in range(n):
    if 0 in box[i]:
        print('-1')
        break
else:
    print(result - 1)

```

- 또한 `deque`로 `import` 해서 쓰는 것이 `que`를 구현할때 시간복잡도가 더 적다는 것을 알았다.



`Python에서 list를 queue처럼 사용할 수 있다. pop(0)를 하면 index 0 에 있는 숫자가 pop된다, 하지만, 이 방법은 O(n)의 시간복잡도로 pop하기 때문에 매우 느리다. 그래서 이 문제에서는 시간초과를 막기 위해 collections의 deque를 사용해야 한다. 해당 자료구조는 O(1)의 시간복잡도로 pop하도록 구현 되어있다.`





#### 2. 나머지

- 트리같은 경우 이번주에 배운 내용인데 벌써 많이 잊어버린듯 하다
- 다음주에 시험이 있으니 다시 복습을 해야겠다.
- 미로 탐색, 단지번호붙이기 같은 경우 `DFS` `BFS`로 쉽해 해결할 수 있었다.