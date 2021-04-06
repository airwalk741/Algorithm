# 4월 6일

### Tree

- 아직 이진트리에 대해 익숙하지 않은 것 같다.
- 학교에서 알고리즘 수업 들었을 때 이해하지 못했던 내용들을 점차 알게 되는 것 같아 신기하다.
- **노드의 합**과 같은 경우 내가 짠 코드 보다는 배웠던 내용을 활용해서 하는 것이 좋은 것 같다.
  - 노드의 왼쪽, 오른쪽 자식을 나누어 연산

```python

def search(idx):

    if idx >= n + 1:
        return 0
    if tree[idx]:
        return tree[idx]
    left = idx * 2
    right = left + 1
    result = search(left) + search(right)
    return result

```

- **이진 힙** 같은 경우 부모, 왼쪽자식, 오른쪽 자식 이렇게 3개씩만 보면 되기 때문에 굳이 `idx==1`까지 가서 오른쪽 트리까지 확인할 필요가 없음을 알게 되었다.
  - 수정된 코드

```python
def left(idx):

    if idx == 1:
        # right(1)
        return
    if tree[idx] < tree[idx//2]:
        tree[idx], tree[idx//2] = tree[idx//2], tree[idx]
        left(idx//2)
```



- **사칙 연산** 도 마찬가지로 왼쪽자식, 오른쪽 자식을 나누어 계산하자





### Study-TEST

- `BFS` `DFS`가 아직 익숙하지 않다
- 특히 `DFS`에서 많이 해멘다
- 연습이 필요한 것 같다
- `트리의 부모 찾기`같은경우 오늘 배운 트리를 이용하려 했지만 오늘은 이진 트리만 배웠기때문에 할 수 없음을 알고 `DFS`로 해결하고자 했다
  - 하지만 메모리 초과 발생
  - 메모리 초과는 처음봐서 생소하다.