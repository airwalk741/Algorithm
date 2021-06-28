# 4월 5일

#### 1. 바이러스

- 무방향성이기 때문에 연결된 컴퓨터를 각각 1로 체크 해줬어야했는데 한 곳만 체크해서 `fail`했다

```python
def dfs(idx):
    global cnt

    visited[idx] = 1
    s = [idx]

    while len(s):

        num = s.pop()

        for i in range(v+1):
            if computer[num][i] or computer[i][num]:
                if visited[i] == 0:
                    visited[i] = 1
                    s.append(i)
                    cnt += 1
```

- 대신에 아래 코드 `if`문을 주어 양쪽 다 탐색하도록 하게 만들었다.

```python
if computer[num][i] or computer[i][num]:
```





#### 2. 미로탐색

- `델타`를 사용할때 가장 중요한 범위 체크를 하지않아 첫 시도에서 `fail` 을 했다.

- 아래 코드를 추가해서 `pass`

```python
 if -1 < x < r and -1 < y < c: # 맵 안쪽의 인덱스인지 확인
```





#### 3.  DFS와 BFS

- 1번과 마찬가지로 무방향이기 때문에 연결된 노드에 각각 `1`을 주었어야했는데 한 쪽만 `1` (연결됐다고)해서 `fail`이 났었다.
- 수정전

```python
for i in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1
```

- 또한 노드가 1번부터 있어 `n+1` 까지 탐색을 해줬어야했는데 `DFS`에서 실수로 `n`까지 탐색하게 코드를 구현하여 계속 `fail` 했다



#### 4. 단지번호 붙이기

- SWEA의 지뢰찾기와 비슷한 풀이로 풀었다.
- 2번과 마찬가지로 범위체크를 하지 않아 엉뚱한 결과가 나왔었다.





```
실수 체크

1) 무방향이라면 양쪽 다 갈 수 있음을 체크해주기
2) 델타 이용시 꼭 범위 체크해주기
```

