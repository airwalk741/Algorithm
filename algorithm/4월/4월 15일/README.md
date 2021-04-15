# 4월 15일

#### 화물 도크

- 나는 시작시간을 정렬해서 `DFS`로 풀었는데 이게 아니였다.
- 처음 생각한 것처럼 푸는 방식이 맞는데 시작시간이 아닌 종료시간에 정렬하는 것이였다

```python
T = int(input())

for tc in range(1, 1+T):
    print('#{}'.format(tc), end=' ')
    n = int(input())

    arr = []

    for i in range(n):
        arr.append(list(map(int, input().split())))

    arr.sort(key=lambda x: x[1])

    s = arr[0][1]
    cnt = 1

    for i in range(1, n):
        if s <= arr[i][0]:
            s = arr[i][1]
            cnt += 1

    print(cnt)
```

- 이렇게 작성하게 되면 내가 구현 한 코드보다 훨씬 간결하고 쉽게 구현하는 것이다....
- 막히게 되면  오류를 찾기 위해 다른 방법을 시도하는 것도 좋지만, 아예 코드를 지워서 새롭게 시작하는 것도 좋은 것같다...



#### 치즈

- 입력 행렬을 늘렸기 때문에 상하좌우 할때 범위값도 같이 수정을 해야 했다.
- 문제는 가로와 세로 두개의 값이 다르게 주어지는데 **가로 = 세로**라고 생각하고 풀었다가 시간초과가 발생했다.
- 처음에 시간 초과가 났기때문에 `bfs`구현이 잘 못 된줄알고 다른 방법 찾다가 좀 좋은 코드가 된거 같아 뿌듯한다.
- 구글링해서 찾은 코드는 `(0, 0)` 지점을 반복해서 찾는 것이고 내가 구현한 코드는 한번만 `(0, 0)` 지점에서 탐색하고 그 이후에는  찾은 지점들을 모아 굳이 탐색 하지 않아도 될 부분을 배제해 시간이 적게 걸리게끔 구현했다.



- **구글링 코드**

```
import sys
from collections import deque

# 위 - 오 - 아래 - 왼 순서
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

H, W = map(int, sys.stdin.readline().split(" "))
field = []

for _ in range(H):
    field.append(list(map(int, sys.stdin.readline().split(" "))))

left = 0
for i in range(H):
    for j in range(W):
        if field[i][j] == 1:
            left += 1

def bfs(left):
    while queue:
        now = queue.popleft()

        for i in range(4):
            ndr = now[0] + dr[i]
            ndc = now[1] + dc[i]

            if 0 <= ndr < H and 0 <= ndc < W and visited[ndr][ndc] == 0:
                visited[ndr][ndc] = 1

                # 치즈 가장자리를 만나면
                if field[ndr][ndc] == 1:
                    field[ndr][ndc] = 2
                    left -= 1
                else:
                    queue.append([ndr, ndc])

    return left


def delete():
    for i in range(H):
        for j in range(W):
            if field[i][j] == 2:
                field[i][j] = 0

queue = deque()

count = 0
temp = left
while left != 0:
    visited = [[0 for _ in range(W)] for _ in range(H)]
    queue.append([0, 0])
    visited[0][0] = 1
    left = bfs(left)

    if left != 0:
        temp = left

    count += 1
    delete()

print(count)
print(temp)
```



- 출처

https://yuuj.tistory.com/93