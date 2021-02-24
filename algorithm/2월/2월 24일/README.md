# 2월 24일 

#### 1. 검정문제 예시 (기지국)

- 테스트 케이스가 한개뿐이여서 보충시간에 풀었을 때 맞은 줄 알았는데 `if`문을 좀 줄일려고 하다보니 오류가 발생했었다.
- **처음 작성했던 부분**

```python
if arr[i][j] == 'A':
    for k in range(3):
        if 0 <= i-1+k < n and 0 <= j - 1 + k < n:
            if arr[i - 1 + k][j] != 'B' or arr[i - 1 + k][j] != 'C':
                arr[i - 1 + k][j] = 'x'
                arr[i][j - 1 + k] = 'x'

elif arr[i][j] == 'B':
    for k in range(5):
        if 0 <= i - 2 + k < n and 0 <= j - 2 + k < n:
            if arr[i - 2 + k][j] != 'A' or arr[i - 2 + k][j] != 'C':
                arr[i - 2 + k][j] = 'x'
                arr[i][j - 2 + k] = 'x'

elif arr[i][j] == 'C':
    for k in range(7):
        if 0 <= i - 3 + k < n and 0 <= j - 3 + k < n:
            if arr[i - 3 + k][j] != 'A' or arr[i - 3 + k][j] != 'B':
                arr[i - 3 + k][j] = 'x'
                arr[i][j - 3 + k] = 'x'
```

- 행과 열의 조건문을 따로 줘서 값을 바꿔야 했었는데 잘 못 구현하였다.
- 이렇게 구현하면 행 또는 열이 어떠한 조건에 맞지 않아져서 **H**가 **x**로 바뀌지 않는다.
- 또한, 기지국 마저 **x**로 바뀌는 경우도 생기게 된다.



#### 2. 스도쿠 검증

- **전에 했던 코드**

```python
# 3 X 3 행렬을 나눈 것
for x in range(0, 7, 3): # 행 기준 자리 바꾸는 것
    for k in range(0, 7, 3): # 열 기준 자리 바꾸는 것
        count_r = [1] * 10
        for i in range(x, 3+x): # 3 X 3 행
            for j in range(k, 3+k): # 3 X 3 열
                count_r[arr[i][j]] -= 1

        if count_r.count(1) != 1:
            result = 0
            break
    if result == 0:
        break
```

- 확실히 한번 더 푸니까 

```python
for i in range(x, 3+x): # 3 X 3 행
    for j in range(k, 3+k): # 3 X 3 열
```

- 위와 같이 범위 실수를 하지 않는 것 같다.



#### 3. 어디에 단어가 들어갈 수 있을까

- 가장 첫번째로 풀었을때를 좀 더 간단하게 풀었어야하는데...
- 3번째 풀지만 계속 `count`에서 `k` 값을 벗어나면 어떻게 해야하지라는 틀에 박혀있는 것같다....

- **좀 더 간단한 코드**

```python
for i in range(n):
    cnt = 0
    # 벽을 한칸 더 늘렸기 때문에 증가
    for j in range(n+1):
        if puzzle[i][j]:
            cnt += 1
        else:
            if cnt == k:
                ans += 1
            count = 0

    for j in range(n+1):
        if puzzle[j][i]:
            cnt += 1
        else:
            if cnt == k:
                ans += 1
            count = 0
```

- 코드로 막 써내려하지말고 생각하고 오류를 찾아내자...



#### 4.  농작물 수확하기

- 처음 풀때보다 쉽게 푼거같다.

- `k`라는 변수를 전보다 잘 활용한 것 같다.

- **전의 코드**

```python
# 밑 부분 더하는 것
k = 1
for i in range(n//2+1, n):
    # 중간지점 찾아서 양쪽으로 줄어들게 끔
    for j in range(i-(n//2), n-k):
        result += arr[i][j]
    k += 1
```





```
분명 면접 볼때 알고리즘 풀때 먼저 생각을 하고 코드를 써내려가는 시간이 좋다고 
말을 했었는데 그때 면접관님은 왜 문제 풀때는 먼저 하나라고 써내려가야한다고 했을까
나도 그 대답을 받고 말도 안되는 답변을 했었느데
오늘 생각해보면 그냥 내 생각이 맞는 것 같다.
생각하지 않고 일단 써내려가면 이상한 코드만 작성되고 하나하나 늘려나가다보면
긴 코드가 아까워 더 시간을 투자하다 시간만 버리는 느낌이다.
파이프 문제처럼 먼저 손으로 풀고 해봐야겠다...
```

