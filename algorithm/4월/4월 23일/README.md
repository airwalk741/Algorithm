# 4월 23일



### 창용 마을 무리의 개수

- `find_set()`을 알지 못했을때는 `dfs`를 사용해서 연결된 사람끼리 하나로 묶어줬었다
- `find_set()`을 알고나니 문제가 너무 쉽게 느껴졌다....

- **알지 못했을때 코드**

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
                if arr[x][i]:
                    s.append([x, i])
                if arr[i][x]:
                    s.append([i, x])
 
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



- **다익스트라** 와 **kruskal** 를 좀 더 복습해야 할 것같다.
- **find_set(), union()**도 마찬가지로 익숙해질 때까지 잘 복습해보자

