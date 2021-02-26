# 2월 26일

#### 1. 손익 분기점

- 백준은 시간을 많이 쓰면 안되나 보다...
- 처음 코드 작성한거 맞긴한데 쓸데 없는 반복때문에 시간초과로 **fail** 이 나왔다.
- **처음 작성한 코드**

```python
a, b, c = map(int, input().split())

if b > c:
    print('-1')
else:
    i = 1
    while True:

        if a + i * b < c * i:
            break
        i += 1
    print(i)
```



#### 2. 8진수 2진수

- 파이썬 문법을 알아야 풀 수 있는 문제지 않을까 싶다.
- `bin`함수만 써서 작성해서 8진수를 2진수로 바꿀려고 했는데 또 **시간초과**가 떴다.
- 그럼.. 문법을 알아야 풀 수 있지않나...
- **처음 작성한 코드**

```python

n = list(input())
result = ''

while len(n):
    num = bin(int(n.pop(0)))
    a = num[2::]
    if len(a) == 1:
        a = '00' + a
    elif len(a) == 2:
        a = '0' + a

    result += a

if result[0] == '0':
    print(result[1::])
else:
    print(result)
```



```
2번과 같은 문제가 나오면 어떻할까 
시간초과만 아니면 풀 수 있는데 지금은 문제가 되지않지만 나중에 큰 걸림돌이 되지 않을까싶다
2번 문제처럼 쉬워도 차근차근 알아가자라고 생각하면서 기억해야겠다.
(오늘은 IM 시험을 봤음(PASS))
```



