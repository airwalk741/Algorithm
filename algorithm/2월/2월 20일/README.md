# 2월 20일

#### 1.  두개의 숫자열

- n 과 m에 길이에 따라서  for문 인자가 바뀔 것 같아 함수를 이용해서 풀었다.
- 라이브 강의 때 교수님이 `n-m+1`  자주 쓸거라고 했는데 이 문제를 통해서 무슨 느낌인지 알 것 같다.

```python
for i in range(m-n+1):
    result = 0
    for j in range(n):
        result += (a[j] * b[i+j])
    if result_max < result:
        result_max = result
```



#### 2. Sum

- 이 문제는 처음 풀때와 같은 접근으로 풀었는데 이 방법뿐인 것 같다.
- 처음과 다른것은 for문을 전보다 적게 썼다.
- 하나의 for문 안에서 가로, 세로, 대각선, 반대 대각선을 구하였다.

**처음 풀었을 때**

```python
for i in range(100):
    arr_sum = 0
    for j in range(100):
        arr_sum += arr[i][j]   #가로 합

    if arr_max < arr_sum:
        arr_max = arr_sum
    # 대각선 합
    if i == j:
        arr_sum1 += arr[i][j]

    if arr_max < arr_sum1:
        arr_max = arr_sum1

# 반대 대각선 합
for i in range(100):
    arr_sum2 += arr[i][99-i]

    if arr_max < arr_sum2:
        arr_max = arr_sum2

# 가로의 합
for j in range(100):
    arr_sum = 0
    for i in range(100):
        arr_sum += arr[i][j]
    if arr_max < arr_sum:
        arr_max = arr_sum
```



#### 3. Ladder1

- 처음 풀었을 떄는 위에서부터 아래로 내려가는 방식으로 풀었었다.

- 사다리게임 하면은 항상 밑에서 위로 보곤 했었는데 왜 처음 이 문제를 접했을 때는 그 생각을 못했을까..

- 첫번째 풀 때는 왼쪽이나, 오른쪽으로 가다가 아래에  **1**이 있으면 내려가게 설정했었는데 현재 위치(인덱스)를 조절하지 않아서 왼쪽으로 갔다가 다시 오른쪽으로 돌아가는 오류가 발생했었다.

- 두번째 풀 때는 왜 그랬는지 모르겠는데 현재 위치에서 왼쪽 오른쪽을 보지 않고

  바로 위에서 왼쪽 오른쪽을 비교해서 **1**이 있으면 그쪽으로 가는 방향으로 했다.

- 그렇게 하면 아래와 같은 사다리에서 오류가 발생한다.

```python
0 0 0 0 1 0 1 0
0 0 0 0 1 0 1 0
0 0 0 0 1 0 1 0
0 0 0 0 1 1 1 0
1 1 1 1 1 0 0 0
```

**오류가 났던 코드 **

```python
while j > 1:
   # 위쪽으로 이동했을 때 왼쪽에 1이 있다면
    if puzzle[j-1][i-1] == 1:
        i -= 1
        j -= 1
        while puzzle[j-1][i] != 1:
            i -= 1
   # 위쪽으로 이동했을 때 오른쪽에 1이 있다면
    elif puzzle[j-1][i+1] == 1:
        i += 1
     	j -= 1
        while puzzle[j-1][i] != 1:
            i += 1
    j -= 1
break
```



#### 4. 파리퇴치

- 쉬워서 패스



#### 5. String

- 하... 문제는 오류 찾으면서 하면은 금방 풀 수 있겠는데...
- 입력값을 다른 문제들처럼 text에 담에서 풀면 오류가 발생해서 코드가 돌아가지 않는다...

```python
import sys
sys.stdin = open('input (6).txt', 'r')
```

- 처음 풀었을때도 그랬는지 저 두 문장을 주석 처리하고 복붙해서 입력한 것 같다...

```bash
Traceback (most recent call last):
  File "C:/Users/park/PycharmProjects/pythonProject/연습/2월 20일/string.py", line 7, in <module>
    t = int(input())
UnicodeDecodeError: 'cp949' codec can't decode byte 0xec in position 5091: illegal multibyte sequence
```

- 이러한 오류가 뜨는데 text에서 `,` `.` `?`  와 같이 특수 문자들을 다 공백처리 해줬더니 그제서야  돌아갔다.. 
- `cp949` 이거 검색해서 찾아보면 사람들이 파일 위치를 잘못한거라는데 뭐지..

- 코드에서 오류는 주석에 적은것과 같이 **tti**에서  오류가 발생하지않도록 조건문을 하나 더 추가해서 문제를 해결하였다.





```
오늘은 코드 짜면서 벌레? 그모양을 좀 자주 사용했다. 다음주에 있을 시험에서 벌레를 써도 된다고 해서 좀 익숙하게 다뤄야 시험때 당황하지 않을 것같아 사용했다. 사실 전에는 공책으로 하나하나 계산하면 귀찮아서 파이썬 튜터를 많이 이용했는데 이 벌레 모양이 그거랑 유사해서 벌레를 쓰는걸 우선적으로 해야겠다.(시험때도 쓸 수 있으니까)
오늘은 토요일이라 좀 느슨하게 했다. 주말이 제일 좋다 평일 너무 힘들어
```

















