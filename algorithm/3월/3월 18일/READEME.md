# 3월 18일

### 추억의 2048 게임

- `up`과 `down`은  시계 반대방향으로 90도 뒤집으면 각각 `left`, `right`와 같다.
- 처음에 `right`에서 0을 만나면 `pop()`를 하고 뒤에 바로 `append(0)`을 해줬었는데 인덱스 접근에서 오류가 있었나보다

- **처음 작성코드**

```python
 if s == 'up' or s == 'left':
        for i in range(int(n)):
            for j in range(int(n)-1):
                if arr[i][j] == 0:
                    arr[i].pop(j)
                    arr[i].append(0)

        for i in range(int(n)):
            for j in range(int(n)-1):
                if arr[i][j] == arr[i][j + 1]:
                    arr[i][j] += arr[i][j]
                    arr[i].pop(j + 1)
                    arr[i].append(0)
```

```
4 8 0 4 1
4 4 2 0 8
8 0 8 4 4
8 2 0 2 8
0 2 0 0 1
```

- 이 입력에서 오류가 발생

- **두 번째 작성코드**

```python
 if s == 'up' or s == 'left':
        # 0이 있다면 다 오른쪽으로 가야한다.
        for i in range(int(n)):
            j = 0
            while j < len(arr[i]):
                if arr[i][j] == 0:
                    arr[i].pop(j)
                else:
                    j += 1
```

- 마찬가지로 위의 테스트케이스에서 오류가 나온다.



- **세번째 코드**

```python
 elif s == 'down' or s == 'right':


        for i in range(int(n)):
            for j in range(int(n)-1, -1, -1):
                if arr[i][j] == 0:
                    arr[i].pop(j)

        for i in range(len(arr)):

            for j in range(len(arr[i])-1, 0, -1):
                if arr[i][j] == arr[i][j-1]:
                    arr[i][j] += arr[i][j]
                    arr[i].pop(j-1)
                
            arr[i] = [0] * (int(n)-len(arr[i])) + arr[i]
```

```
4 8 0 4 1
4 4 2 0 8
8 0 8 4 4
8 0 0 2 2
0 2 0 0 1
```

- 입력 값에서 오류







```
2차원 배열에서 값을 제거했을 때 오른쪽부터 접근과 왼쪽부터 접근에 따라
다음 인덱스가 어떻게 바뀌는지 보는 문제였다
저번에 2시간 동안 못풀었는데
오늘 10분정도만에 오류 찾아서 풀었다.
```





