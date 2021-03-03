# 3월 3일

#### 1. BFS

- DFS코드에서 `pop(0)` 이부분만 고쳤는데 너비우선 탐색이 구현되었다

- **DFS 코드**

```python
def dfs(v): # 반복구조의 dfs
    res=[] # 방문순서를 저장할 리스트
    s = [] # 스택 생성
    s.append(v) # push(v) 시작점 저장

    while len(s)!=0: # 스택이 비어있지 않으면
        n = s.pop() # pop(), 갈 수 있는 노드 중 하나를 꺼내 이동

        if visited[n] == 0:
            visited[n] = 1  # 방문했음을 표시
            res.append(n)
            for i in range(N+1):
                if adj[n][i]==1: # i가 인접하면
                    s.append(i) # 인접 목록 추가
    return res
```



```
큐를 작성한는데 파이썬 내장함수 append() 와 pop()가 있어서 딱히라는 생각이 들었다.
다른 방식으로도 해봐야하나보다
백준은 어떤 문제를 풀어야할지 모르겠다
랭크가 브론즈4이길래 그 문제들을 풀어보는데 기본문제들같다
어떻게 해야하지
그냥 일단 내일부터는 swea를 풀어야겠다
```

