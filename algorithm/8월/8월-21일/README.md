# 8월 21일

## 🚩 이모티콘

[![image-20210821161517219](README.assets/image-20210821161517219.png)](https://www.acmicpc.net/problem/14226)



#### ✍ 풀이

- `BFS`를 이용해 스크린과 S의 개수가 같을 때를 찾는다.
- `연산1`과 `연산3` 덕분에 방문 체크를 하지 않으면 무한 루프를 돌게 된다.
- `연산1` 때문에 2차원 배열을 사용하게 될텐데 뭔가 메모리 초과 발생할 것 같아 1차원 배열을 이용하고자 했다.
- 근데 생각해보니까  ` (2 ≤ S ≤ 1000) `이므로 2차원 배열 풀이가 더 맞는 것 같다.
- 나는 클립보드와 스크린이 다르기 때문에 또한, 구하고자 하는 것이 스크린의 이모티콘 수이기 때문에 클립보드가 변한다면 방문 체크를 해주었다. 
- 스크린이 변할 때 방문 체크를 해준다면 `연산 1`을 했을 때 무조건 `q`에 들어가지 않아 잘 못 된 값이 나온다.
- 최솟값을 구하는 것이기 때문에 `cnt`를 비교해 크면 `PASS`했다.



#### 👍 다른 풀이

- 2차원 풀이

```python
import sys
from collections import deque

s = int(sys.stdin.readline().rstrip())

def isin(y,x):
    if y < 1500 and x < 1500: return True
    return False

def solve():
    visited = [[False for _ in range(1500)] for _ in range(1500)]
    q = deque()
    # 시간, 화면에 출력되는 이모티콘, 클립보드에 저장된 이모티콘
    q.append([0, 1, 0])
    visited[1][0] = True

    while q:
        sec, scnt, ccnt = q.popleft()
     
        if scnt == s:
            print(sec)
            break

        # 화면에 있는 이모티콘을 클립보드에 복사
        next_ccnt = scnt
        if not visited[scnt][next_ccnt]:
            visited[scnt][next_ccnt] = True
            q.append([sec+1, scnt, next_ccnt])

        # 클립보드에 있는 이모티콘을 화면에 복사
        if ccnt > 0:
            next_scnt = scnt + ccnt
            if isin(next_scnt, ccnt) and not visited[next_scnt][ccnt]:
                visited[next_scnt][ccnt] = True
                q.append([sec+1, next_scnt, ccnt])
        
        # 화면에 있는 이모티콘 제거
        if scnt > 1:
            next_scnt = scnt - 1
            if isin(next_scnt, ccnt) and not visited[next_scnt][ccnt]:
                visited[next_scnt][ccnt] = True
                q.append([sec+1, next_scnt, ccnt])
            
solve()
```



