# 8월 13일

## 🚩 점프

[![image-20210813211130375](README.assets/image-20210813211130375.png)](https://www.acmicpc.net/problem/1890)

#### ✍ FAIL

- 경로의 개수가 2^(63 - 1)이기 때문에 `dfs`, `bfs`로 해결하면 안된다.

- `DP`로 해결해야한다.
- `DP` 활용 잘 못하겠다..
- 처음에는 목적지까지 가고 도착 했다면 그 전단계를  `+1` 해줬다.
- 다음 `TC` 부터는 방문이 되어있으면 `Stack`에 담지 않고 `result`에만 추가 시켜줬다.
- 아래 `tc`에서 `fail`

```
11
1 1 2 2 3 3 3 3 2 3 1
1 1 3 2 2 2 3 1 3 2 3
1 3 3 2 2 2 3 3 2 2 1
3 2 2 3 2 3 1 2 3 1 1
3 1 3 3 3 1 2 1 3 3 2
3 1 1 3 3 1 2 3 3 1 1
3 2 2 1 1 1 2 1 1 3 2
2 2 3 2 1 1 2 3 2 2 3
3 3 1 3 2 1 3 1 1 2 2
3 3 3 2 3 2 2 3 2 1 3
2 2 1 2 3 3 2 2 1 1 0

output = 232
```



```python
import sys
sys.stdin = open('input.txt', 'r')
import pprint

def search(r, c, cnt):
    global result


    s = [(r, c, cnt)]

    while s:

        r, c, cnt = s.pop()

        if not cnt:
            continue

        for i in range(2):

            if not i:
                x = r
                y = c + cnt
            else:
                x = r + cnt
                y = c

            if x < n and y < n:
                if x == n - 1 and y == n - 1:
                    visited[r][c] += 1
                    result += 1
                    continue
                else:
                    if visited[x][y]:
                        visited[r][c] += 1
                        result += visited[x][y]
                    else:
                        s.append((x, y, arr[x][y]))


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

result = 0
visited = [[0] * n for _ in range(n)]
visited[n-1][n-1] = 1
search(0, 0, arr[0][0])
print(result)


```

