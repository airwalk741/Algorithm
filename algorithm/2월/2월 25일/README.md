# 2월 25일

- 오늘은 실습문제를 잘 풀지 못해서 멘탈도 나가고 머리를 좀 많이 쓴 기분이 들어서 어지럽다..
- 실습 문제중에서 **자기 방으로 돌아가기** 와 **재미있는 오셀로 게임**에서 시간을 정말 많이 썼다.
- **자기 방으로 돌아가기**는 해결 했지만 **재미있는 오셀로게임**은  해결하지 못하였다.
- 내일 시험을 끝내고 **델타** 활용하는 연습과 **스택**, **퀵정렬** 복습을 해야겠다.



#### 1. 세로로 말

- 스택을 배운김에 스택을 활용한건지는 모르겠지만, `pop()`을 써서 인덱스 조절하는 연습을 해보았다.
- 확실히 공책에 쓰면서 하니까 빨리 풀 수 있게 되었다.
-  **처음에 풀었던 코드**

```python
T = int(input())
 
for tc in range(1, T+1):
 
    arr = [list(input()) for _ in range(5)]
 
    max_idx = 0
    for i in range(len(arr)):
        if max_idx < len(arr[i]):
            max_idx = len(arr[i])
 
    print('#{}'.format(tc), end=' ')
 
    for i in range(max_idx):
        for j in range(5):
            if i > len(arr[j])-1:
                if len(arr[j]) < max_idx:
                    continue
 
            print(arr[j][i], end='')
 
    print()
```



#### 2. 정곤이의 단조 증가하는 수

- 처음 풀었을때는 리스트에 담아서 정렬을 시킨 뒤 정렬하지 전의 리스트와 비교해서 단조 숫자인지 확인하는 소스를 구현하였다.
- 타임에러가 발생할 것같긴했는데 역시나였다.
- 리스트 말고 인덱스 접근할 수 있는 것을 생각하다가 문자열이 떠올라 작성하였다.
- 문자열로 변환했기때문에 나중에 저장할때는 꼭 `int`형으로 변환해서 저장해야한다.
- **타임에러 발생한 코드**

```python
T = int(input())
 
for tc in range(1, T + 1):
 
    n = int(input())
 
    arr = list(map(int, input().split()))
 
    result = []
 
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            number = arr[i] * arr[j]
            num = arr[i] * arr[j]
            a_list = []
            while num > 0:
                a_list += [num % 10]
                num = num // 10
 
            a_list = list(reversed(a_list))
            b_list = sorted(a_list)
            for k in range(len(a_list)):
                if a_list[k] != b_list[k]:
                    break
            else:
                result += [number]
 
    print('#{}'.format(tc), end=' ')
    if len(result):
        print(max(result))
    else:
        print('-1')
```



```
평소에도 느꼈지만 다들 잘 하는 것 같다.
나는 뭔가 돌아가서 푸는 느낌인데 작성한 코드를 보면 다들 쉬운 방법을 찾아
쉽게 작성하더라..
부럽다.. 잘해서... 델타나 슬라이싱 같은거 활용도 잘하고 저번에는 객체 이용한걸로 푼거보고
와... 싶었다.. 나는 다 까먹은거같은데,..
web 하기 전에 복습 해두어야겠다.
오늘은 어지러워서 일찍자야지..
```

