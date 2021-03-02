# 3월 2일

#### 1.  배열 최소 합

- 두 가지 방법으로 풀었다 하나는 순열로 인덱스를 구해서 `sum`을 하는 방법,

  다른 하나는 **dfs**를 이용해서 인덱스가 확인되면 바로 더해줘서 최솟값을 찾는 방법으로 구했다.

- ** dfs를 이용한 방법 **

```python
def dfs(value, _sum):
    global _min
    # value => 행
    # _sum => 구하는 최소값
    # 마지막 열이라면 최솟값을 비교
    if value == n:
        if _sum < _min:
            _min = _sum
        return
    # 백트레킹 ( 굳이 안해도 되는 연산 제거 )
    if _sum >= _min:
        return

    for i in range(n):
        # i번째 열을 쓰지 않았다면
        if visited[i] == 0:
            visited[i] = 1 # 썼다고 하고
            dfs(value + 1, _sum + arr[value][i]) # 다음 행으로 옮기는 재귀함수로
            visited[i] = 0 # 다시 원래대로 
    return _min


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    print('#{}'.format(tc), end=' ')

    arr = [list(map(int, input().split())) for _ in range(n)]

    # 열 방문했는지 안했는지 체크하는 변수
    visited = [0] * n

    _min = 987654321

    print(dfs(0, 0))

```

- 순열로 구하게 되면 쓸데 없는 풀이까지 하게 되어 시간초과가 발생한다.
- **dfs**에서도 마찬가지이지만 중간에 쓸데 없는 풀이를 하지 않게끔 **if**문을 하나 만들어 주었다.

```python
  if _sum >= _min:
        return
```



#### 2.  토너먼트 카드게임

- 학교에서 많이 봤던 문제인데 역시나 기억이 나지 않아 풀지 못했었다.
- **처음 작성한 코드**

```python
def game(a, b):

    global arr

    if arr[a] == 1:
        if arr[b] == 2:
            return b
    elif arr[a] == 2:
        if arr[b] == 3:
            return b
    elif arr[a] == 3:
        if arr[b] == 1:
            return b

    return a

T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')

    n = int(input())

    arr = list(map(int, input().split()))

    result = {}

    for i in range(len(arr)):
        result[i] = arr[i]

    arr_list = [i for i in range(n)]

    while len(arr_list) != 1:

        a = arr_list.pop(0)
        b = arr_list.pop(0)

        arr_list.append(game(a, b))

    print(arr_list[0]+1)
```

- 이렇게 작성하게 되면 짝수끼리 즉 제일 말단 노드가 짝수개로 맞춰줬을 때만 정답이 허용된다.

- 예)

  ![image-20210302215538512](C:\Users\park\AppData\Roaming\Typora\typora-user-images\image-20210302215538512.png)



#### 3. 백준_분산처리

- 잘 풀었었는데 문제를 제대로 읽지 않아 10번째 컴퓨터를 인지하지 못했다.
- 또한 발견하고 나서도 `a`가 10의 배수이면 `0`을 출력하게끔 코드를 구현하여 오류가 발생했다.

- 내가 잘 못한줄 알고 인터넷을 검색해보다가 딕셔너리로 만드는 코드말고 더 좋은 코드를 발견하였다.

```python
result_list = []
temp = 1
for _ in range(b):
    temp *= a
    temp %= 10
    if temp in result_list:
        break
    result_list.append(temp)
```



```
오늘 실습이 제일 어려웠던 것 같다
미로랑 계산기는 저번에 풀어서 쉽게 풀렸는데
순열을 복습을 하지 않아서 하나도 못 풀었다.
복습해야하는데 다른게 더 눈에 들어온다...
```





















