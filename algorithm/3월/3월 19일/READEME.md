# 3월 19일

#### 1. 창용 마을 무리의 개수

- **첫번째**

- 관계가 없는 사람을 생각하지 않았음

```python
def dfs(r, c):
    global cnt
    s = []
    s.append([r, c])

    while len(s):
        x, y = s.pop()

        if arr[x][y]:
            arr[x][y] = 0

            for i in range(n+1):
                if arr[y][i]:
                    s.append([y, i])

    cnt += 1

T = int(input())

for tc in range(1, T+1):

    print('#{}'.format(tc), end=' ')

    n, m = map(int, input().split())

    arr = [[0] * (n+1) for _ in range(n+1)]

    num = []

    for i in range(m):
        num += map(int, input().split())

    no_num = [0] * (n+1)


    for i in range(len(num)):
        no_num[num[i]] += 1

    cnt = no_num.count(0) - 1

    for i in range(0, len(num), 2):
        arr[num[i]][num[i+1]] = 1

    for i in range(n+1):
        for j in range(n+1):
            if arr[i][j]:
                dfs(i, j)

    print(cnt)
```

```
1
7 2
1 3
3 4
```

- 위와 같은 input을 넣으면 5가 나와야하는데 다른값이 나옴





- **두번째**
- `DFS` 생각을 잘 못 해줬음

```python
def dfs(r, c):
    global cnt
    s = []
    s.append([r, c])

    while len(s):
        x, y = s.pop()

        if arr[x][y]:
            arr[x][y] = 0

            for i in range(n+1):
                if arr[y][i]:
                    s.append([y, i])
                if arr[i][y]:
                    s.append([i, y])

    cnt += 1

T = int(input())

for tc in range(1, T+1):

    print('#{}'.format(tc), end=' ')

    n, m = map(int, input().split())

    arr = [[0] * (n+1) for _ in range(n+1)]

    num = []

    for i in range(m):
        num += map(int, input().split())

    no_num = [0] * (n+1)


    for i in range(len(num)):
        no_num[num[i]] += 1

    cnt = no_num.count(0) - 1

    for i in range(0, len(num), 2):
        arr[num[i]][num[i+1]] = 1

    for i in range(n+1):
        for j in range(n+1):
            if arr[i][j]:
                dfs(i, j)

    print(cnt)
```

```
1
5 2
4 1
4 2
```

- 위와 같은 input을 넣어주면 3이 나와야하는데 4가 나옴
- `if`문을 추가해서 해결했음





- 문제점
  - 다른 사람들 코드보다 시간이 더 걸림
  - 다른 코드로 짜봐야겠음