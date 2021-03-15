# 3월 15일

### 1. 가능한  시험 점수

- **DFS**로 풀려고 했는데 시간 초과가 나옴
- **n**의 크기가 100까지여서 그런듯
- **DFS**

```python
def test(index, num):
 
    if index == n:
        if num not in result:
            result.append(num)
        return
 
    test(index+1, num + arr[index])
    test(index+1, num)
 
T = int(input())
 
for tc in range(1, T+1):
 
    print('#{}'.format(tc), end=' ')
    n = int(input())
 
    arr = list(map(int, input().split()))
 
    result = []
    cnt = 0
    test(0, 0)
    print(len(result))
```



###  2. 최대 상금

```python
def max_money(index, number):
    global result
    global change

    if index >= len(number)-1 or index >= change:

        while index < change:
            number[-1], number[-2] = number[-2], number[-1]
            change -= 1

        number3 = int(''.join(number))
        if result < number3:
            result = number3
        return

    for i in range(index, len(number)):
        for j in range(i+1, len(number)):
            number2 = list(number)
            if int(number[i]) < int(number[j]):
                number[i], number[j] = number[j], number[i]


            max_money(index + 1, number)
            number = list(number2)


```

- 이렇게 하면 입력값을 **4321**  **1** 이렇게 하면 결과가 **4312**로 나와야하는데 **4321**나온다



```python
def max_money(index, number):
    global result
    global change
    change1 = change
    if index == len(number)-1 or index == change1:

        while index < change1:
            number[-1], number[-2] = number[-2], number[-1]
            change1 -= 1

        number3 = int(''.join(number))
        if result < number3:
            result = number3
        return

    for i in range(index, len(number)):
        for j in range(i+1, len(number)):
            number2 = list(number)
            if int(number[i]) < int(number[j]) or change == 1:
                number[i], number[j] = number[j], number[i]
            max_money(index + 1, number)
            number = list(number2)


```

- 이렇게 코드를 작성하면 위에 예시 입력값은 잘 나오지만

  입력값이 **77732**  **1** 이렇게 나오면 출력이 **77732** 로 나온다



```python
def max_money(index, number):
    global result
    global change
    change1 = change
    if index == len(number)-1 or index == change1:

        while index < change1:
            number[-1], number[-2] = number[-2], number[-1]
            change1 -= 1

        number3 = int(''.join(number))
        if result < number3:
            result = number3
        return

    for i in range(index, len(number)):
        for j in range(i+1, len(number)):
            number2 = list(number)
            if int(number[i]) == int(number[j]):
                continue
            if int(number[i]) < int(number[j]) or change == 1:
                number[i], number[j] = number[j], number[i]
            max_money(index + 1, number)
            number = list(number2)
```

- 이렇게 작성했을 때는 위에 2개의 테스트케이스는 통과하지만

  **8번째 테스트케이스**에서 오류가 발생했다



- **마지막 코드**

```python
def max_money(index, number):
    global result

    change1 = change
    if index == len(number)-1 or index == change1:

        while index < change1:
            number[-1], number[-2] = number[-2], number[-1]
            change1 -= 1

        number3 = int(''.join(number))
        if result < number3:
            result = number3
        return

    for i in range(index, len(number)):
        for j in range(i+1, len(number)):
            number2 = list(number)

            number[i], number[j] = number[j], number[i]
            max_money(index + 1, number)
            number = list(number2)
```

- 최대값을 구하는 것이기때문에 오른쪽 값이 크면 다음단계로 가는 `if`문을 제거했더는 결과가 잘 나왔다.