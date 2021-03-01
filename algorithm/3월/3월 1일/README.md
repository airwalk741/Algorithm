# 3월 1일

#### 1. 계산기2

- 처음에 작성했을때는 **스택** `st`에 남은 것들을 뒤에서부터 꺼냈어야 했는데 앞부터 꺼내서 후위 표기법을 했었다.
- 이것 때문에 실습시간에 많이 해맸다가 다른 동기가 작성한 코드보고 '아 여기서 잘 못했었구나...'하고, 오류를 찾아 올바른 코드를 작성했다.

- **처음 작성했던 코드**

```python
while len(st) > 0:
    result.append(st.pop(0))
```

- 후위 표기법 우선 순위  => **같거나 크면 스택에서 뺀다**



#### 2. 길찾기

- **dfs**를 이용해서 풀이 하는 것이다.
- 이상하게 학교 다닐땐 코드 한줄도 작성하지도 못했었는데 이렇게 풀이도 할 수 있다니.. 신기하다
- **dfs**

```python
def dfs(value):

    result = []
    st = []
    st.append(value)

    while len(st) > 0:

        n = st.pop()
        if visited[n] == 0:
            visited[n] = 1
            result.append(n)
            for i in range(len(arr_list)):
                if arr_list[n][i] == 1:
                    st.append(i)
    return  result
```



```
학교 다닐때보다는 코드 작성하는게 괜찮아진거같은데 또 백준이나, SWEA를 풀어보면 아닌거같다..
얼마나 공부를 대충했으면 그럴까..
한문제라도 이렇게 복습 차원에서 코드 작성해야겠다
언젠간 나도 실력이 늘겠지..
```



