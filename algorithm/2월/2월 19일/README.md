# 2월 19일

#### 1. 파스칼의 삼각형

- 출력 부분에서 시간을 많이 썼다

**수정 전**

```python
print('1', '{} '.format(i-1)*(i-2), '1' )
```

**결과**

```python
1
1 1
1 2 1
1 33 1
1 444 1
```

- 이런 형태로 나와 문제에 맞는 출력이 아닌라 라인을 더 쓰는 대신 원하는 출력에 맞춰 출력하였다.

**수정 후**

```python
print('1',end=' ')
print('{} '.format(i-1)*(i-2), end='')
print('1')
```

- 더 깔끔한 방법이 있을 것 같아 다른 코드들을 봤는데 어려워서 이렇게 하는게 나은거 같다.



#### 2.  View

- 처음 작성했던 코드

```python
for j in range(1, 11):

    length = int(input())

    a = list(map(int, input().split()))

    result = 0

    for i in range(length):
        a_min = 0
        b_min = 0

        if i == 0:
            if a[i+1] < a[i+2]:
                a_min = a[i] - a[i+2]
            else:
                a_min = a[i] - a[i+1]

            if a_min > 0:
                result += a_min

        elif i == 1:

            if a[i+1] < a[i+2]:
                a_min = a[i] - a[i+2]
            else:
                a_min = a[i] - a[i+1]

            if a_min > (a[i] - a[i-1]):
                a_min = (a[i] - a[i-1])

            if a_min > 0:
                result += a_min

        elif i == (length-1): # 100 -1
            if a[i-1] < a[i-2]:
                a_min = a[i] - a[i-2]
            else:
                a_min = a[i] - a[i-1]

            if a_min > 0:
                result += a_min

        elif i == (length - 2): # 100 - 2
            if a[i - 1] < a[i - 2]:
                a_min = a[i] - a[i - 2]
            else:
                a_min = a[i] - a[i - 1]

            if a_min > a[i] - a[i-1]:
                a_min = (a[i] - a[i-1])

            if a_min > 0:
                result += a_min

        else:
            if a[i - 1] < a[i - 2]:
                a_min = a[i] - a[i - 2]
            else:
                a_min = a[i] - a[i - 1]

            if a[i+1] < a[i+2]:
                b_min = a[i] - a[i+2]
            else:
                b_min = a[i] - a[i+1]

            if a_min > b_min:
                a_min = b_min

            if a_min > 0:
                result += a_min

    print(f"#{j} {result}")
```

- 문제를 잘 안읽어보고 input에 들어오는 빌딩 높이 처음과 마지막이 0 이라는 것을 인지 하지 못하고 풀었다.

- 하지만, 인지 했어도 복잡하게 풀었을 것 같다.

- 처음 풀때는 빌딩 왼쪽 2개중 가장 큰 빌딩 찾고, 오른쪽에서도 마찬가지로 가장 큰 빌딩 찾고

  마지막에 두개 빌딩의 크기를 비교해서 큰 빌딩을 찾아 기준 빌딩에서 뺀 값으로 구랬다.

- 두번째 풀때는 좀 다른 방식으로 4개의 if 문을 써서 가장 큰 높이를 찾아 기준 빌딩의 크기에서 뺀 값으로 구했다.

**두번째 풀때**

```python
if max_building < arr[i-2]:
    max_building = arr[i-2]
if max_building < arr[i-1]:
    max_building = arr[i-1]
if max_building < arr[i+2]:
    max_building = arr[i+2]
if max_building < arr[i+1]:
    max_building = arr[i+1]
```



#### 4. 현주의 상자 바꾸기

- 두번째 풀때는 바꿀 상자를 list 형태로 받아와서 풀었다.
- 첫번째 풀때는 while문 안에서 바로바로 받아와서 바꾸는 형태로 풀었다.
- 첫번째 생각한 것이 더 간단한 것 같다.

```python
for tc in range(1, T+1):

    n, q = map(int, input().split())

    result = [0] * n
    count = 1
    # q의 길이만큼 반복
    while q > 0:
        # r, l을 담는다
        r, l = map(int, input().split())
        #  r에서부터 l까지 result를 수정한다.
        for i in range(r-1, l):
            result[i] = count

        count += 1
        q -= 1

    print('#{}'.format(tc), *result)
```



#### 4.  flatten

- 처음 풀때는 높이가 가장 작은 인덱스와 가장 큰 인덱스를 찾아 그 값을 서로 더하고 빼고 하였다.

**처음풀 때**

```python
for j in range(1, 11):

    dump = int(input())

    nums = list(map(int, input().split()))

    # 최소, 최대 높이의 상자들과 그것의 인덱스를 구하기 위해서 변수 선언
    nums_max = nums[0]
    nums_min = nums[0]
    idx_max = 0
    idx_min = 0
    # 최소, 최대 높이의 상자들과 인덱스 구하는 for문
    for index, num in enumerate(nums):
        if num > nums_max:
            nums_max = num
            idx_max = index
        if num < nums_min:
            nums_min =num
            idx_min = index

    # 바꾸는 획수가 0이 될때까지 while문 돈다
    while dump > 0:

        nums[idx_min] += 1 # 제일 작은 상자에는 +1
        nums[idx_max] -= 1  # 작은 상자에 상자 줬으니까 -2
        nums_max -= 1   # 최댓값이 곧 최고 높은 상자인데 하나를 제일 작은 상자에 줬으므로 최댓값도 줄어든다.
        nums_min += 1 # 최대에서 받았으므로 +1
        dump -= 1 # 한번 바꿨으니까 -1

        # 또 찾는거 (최소, 최대)
        for index, num in enumerate(nums):
            if num > nums_max:
                nums_max = num
                idx_max = index
            if num < nums_min:
                nums_min = num
                idx_min = index

    print(f'#{j} {nums[idx_max] - nums[idx_min]}')
```

- 내 생각인데 접근은 좋았는데 인덱스 찾는 것을 함수로 표현하면 뭔가 코드가 간단하지 않았을까 싶다.



#### 5. 삼성시의 버스 노선

```python
  c =[]
    p = int(input())
    for i in range(p):
        c += list(map(int, input()))
```

- c 리스트를 넣을때 이런식으로 작성했는데 잘 못 생각했던것 같다.
- 위와 같이 작성을 하면 입력이 1, 2, 3, 100 이 각각 다른줄로 해서 들어온다면 c에서는 [1, 2, 3, 1]  이렇게 저장이 될 것이다.









```
다음주에 있을 IM 시험때문에 풀었던 문제를 다시 풀고 있지만, 풀었던 코드가 기억이 나지않아 새로운 방법으로 푼 문제들이 있었다. 알고리즘 시작한지 별로 지나지 않았지만 그래도 조금 했다고 2번째 풀때는 좀 간단하게 풀린 것 같다. (물론, 대부분 기억이 나서 그런거지만...)
그래도 어제 오늘 느낀것이 확실이 학교 다닐때보다는 코드 짜는게 많이 늘었던 것 같다.
학교에서 과제로 '쇠막대기 자르기'를 내줬을때는 손도 못댔었는데 이번에는 시간이 좀 걸렸지만 그래도 스스로 풀었다는 거에서 느꼈었다.
README를 두번째 쓰지만 이게 언제까지 갈지 모르겠다. 벌써 귀찮네...
```































