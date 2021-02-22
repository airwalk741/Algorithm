# 2월 22일

#### 1. 영준이의 카드 카운팅

- 딱히 어렵게 풀진 않았는데 소스가 불필요한 부분도 있는거 같다.

- 처음에 풀때는 입력값이 들어오면 그거에 인덱스 하나하나 줘서 숫자값을 비교하였는데

  늘 그랬듯이 또 `slicing`을 사용하지 않아 불필요한 소스가 증가한 것 같다.

- 아래가 처음 작성한 코드이다.

```python
    for i in range(0, len(arr), 3):
 
        if arr[i] == 'S':
            if arr[i+1] == '0':
                s[int(arr[i+2])] += 1
            else:
                s[int(arr[i+2]) + 10] += 1
        elif arr[i] == 'D':
            if arr[i+1] == '0':
                d[int(arr[i+2])] += 1
            else:
                d[int(arr[i+2]) + 10] += 1
        elif arr[i] == 'H':
            if arr[i+1] == '0':
                h[int(arr[i+2])] += 1
            else:
                h[int(arr[i+2]) + 10] += 1
        elif arr[i] == 'C':
            if arr[i+1] == '0':
                c[int(arr[i+2])] += 1
            else:
                c[int(arr[i+2]) + 10] += 1
```



#### 2. 오목판정

- 대각선 오목을 처음에 잘 못생각하고 풀었다.

```python
    if count != 5:
        count = 0
        for j in range(n):
            for i in range(n):
                if j == i:
                    if board[i][j] == 'o':
                        count += 1
                        if count == 5:
                            print('YES')
                            break
                    else:
                        count = 0
            if count == 5:
                break
 
    if count != 5:
        count = 0
        for j in range(n):
            for i in range(n):
                if j + i == n-1:
                    if board[i][j] == 'o':
                        count += 1
                        if count == 5:
                            print('YES')
                            break
                    else:
                        count = 0
            if count == 5:
                break
 
    if count != 5:
        print('NO')
```

- 코드를 보면 `i == j`와  `j == i` 이런식으로 대각선을 구했었다.

- 하필 테스트 케이스도 저렇게 제출을하면 93개가 맞아서 뭐지..? 라는 생각을 하게끔 테스트 케이스를 잡아준거같다...
- 나중에 대각선을 잘못구한걸 캐치하고 다시 코드를 작성했을때는 좌하에서 우상으로 구성된 오목 카운팅을 잘 하지 못하였다.

```python
for i in range(n - 5 + 1):
        for j in range(n-1, n - 5 + 1, -1):
            count_re_cross = 0  # 반대 대각전 오목 확인
            for k in range(5):
                if board[i + k][j - k] == 'o':
                    count_cross += 1
                    if count_re_cross == 5:
                        result = 'YES'
                        break
                else:
                    count_re_cross = 0
 
            if result == 'YES':
                break
        if result == 'YES':
            break
```

- 괜히 끝에서부터 생각하지말고 처음 대각선처럼 앞에서부터 생각했으면 더 편한것 같다. 
- 인덱스를 아직 잘 다루지 못해서 뒤에서부터하면 오류를 잡지 못할 것같다.





```
알고리즘 풀면서 가장 많이 fail이 났던 문제가 오늘 나왔다. 
D3인데 인덱스 개념이 아직 많이 부족한 것 같다. 
금요일 시험이 만약 오늘처럼 나왔다면 시험 부담감이랑 긴장때문에 못풀지 않았을까싶다... 
왜냐하면 오늘도 이상하게 긴장되서 과목평가도 3분 남기도 풀었기 때문이다. 
앞으로 보강이 3번 남았는데 인덱스랑 slicing 을 잘 다뤄바야겠다.
```

