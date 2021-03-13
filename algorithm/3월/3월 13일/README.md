# 3월 13일

## 1. 숫자만들기

- 깊이 우선으로 탐색했으면 돌아올때 그 전에 가지고 있던 값을 가져와야하는데

  처음에는 그 단계를 하지 않아서 계속 오류가 발생했었음

- **처음 코드**

```python
    for i in range(4):
        if operater_num[i] != 0:
            
            if i == 0:
                num = num + number[idx]
            elif i == 1:
                num = num - number[idx]
            elif i == 2:
                num = num * number[idx]
            elif i == 3:
                num = int(num / number[idx])

            operater_num[i] -= 1
            dfs(num, idx+1)
            operater_num[i] += 1
```

- **두번째 코드**

```python
# 연산자 4개 (깊이 우선 탐색)
    for i in range(4):

        if operater_num[i] != 0:
            num2 = num  # 깊이 전 단계를 저장하기 위해 변수 생성
            if i == 0:
                num = operation(num, number[idx], i)
            elif i == 1:
                num = operation(num, number[idx], i)
            elif i == 2:
                num = operation(num, number[idx], i)
            elif i == 3:
                num = operation(num, number[idx], i)

            # num에는 다음단계로 갈 값이 저장되어있음
            # 연산자 하나 썼으니까 -1
            operater_num[i] -= 1
            # 한단계 더 깊이 들어가기
            dfs(idx+1, num)
            # 원상복구
            operater_num[i] += 1
            num = num2
```

- `num2`라는 그 전 단계의 값을 저장할 수 있는 변수를 만들어 놓아 끝까지 탐색하고 `return` 했을 때 그 전단계로 값을 바꿔줬다.





