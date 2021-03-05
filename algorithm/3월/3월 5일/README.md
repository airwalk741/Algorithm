# 3월 3일

- BFS, DFS 연습



#### 1. 햄버거 다이어트

- 부분집합으로 풀면 시간이 오래 걸린다.
- 혹시나해서 정렬을 하고 풀었는데도 마찬가지였다
- 조합을 이용해서 재귀로 풀면 시간이 적게 걸렸다
- **처음 풀었던 코드**

```python
def buble(arr):

    for i in range(len(arr)-1):
        for j in range(i, len(arr)):
            if arr[i][1] > arr[j][1]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

T = int(input())

for tc in range(1, T+1):

    n, l = map(int, input().split())

    gred = [list(map(int, input().split())) for _ in range(n)]

    # 기준 칼로리 넘으면 안되니까 정렬해줘서 for문 적게 계산
    buble(gred)

    res = 0
    # 부분집합
    for i in range(1 << len(gred)):
        kal = 0
        taste = 0
        for j in range(len(gred)):
            if i & (1 << j):
                kal += gred[j][1]
                taste += gred[j][0]
                if kal > l:
                    break

        # 기준 칼로리 넘지 않으면 결과 받음
        else:
            if taste > res:
                res = taste

    print('#{}'.format(tc), end=' ')
    print(res)
```



#### 2. 격자판의 숫자

- 재귀 오류났던 코드

```python
def number(r, c):
	global res
    res += arr[r][c]
    if len(res) == 7:
        if res not in result:
            result.append(res)
        return
    else:
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        for i in range(4):

            dx = r + dr[i]
            dy = c + dc[i]

            if 0 <= dx < 4 and 0 <= dy < 4:
                number(dx, dy)
```

- 어쩌면 당연했던게 `global`을 써서 `res`를 변경하면 7자리를 넘어 더 큰 숫자가 나오기때문에 재귀를 빠져나가지 못하고 폭파(?) 된다.
- 구하는 값까지 아싸리 인자에 추가해서 하자



#### 3. 파핑파핑 지뢰찾기

- 어제 풀지 못했던 문제이다
- 어제 오류를 발견하고 오늘 연습했던 BFS, DFS를 활용해서 풀었다
- 아직 솔직히 반도 모르겠지만 이문제를 통해서 이제야 조금은 알거같다





```
처음에는 할만했던 과정이 어려워진다
2시면 다 풀었던 실습이 엊그제부터 하루종일 해도 못 푸는 문제가 발생한다..
인지는 하고 있었지만 아직 3월인데 벌써부터 어려움이 느껴진다
오늘처럼 비슷한 문제 풀면서 이해해야지..
오늘 3번 풀려서 기분은 좋네
```

