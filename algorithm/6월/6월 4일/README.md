# 6월 4일

## 🚩 

[![image-20210604101949515](README.assets/image-20210604101949515.png)](https://www.acmicpc.net/problem/11047)



### ✍ 풀이

- 찾는 금액보다 작고 가장 큰 동전을 나눠 계산 후 출력하기



### 😒 fail 이유

- 처음에 찾는 금액보다 큰 값을 찾아서 그 전 인덱스로 나눠서 계산했다.
-  `K`보다 큰 동전이 없을 수도 있다는 것을 생각하지 않아서 `FAIL`이 났다.





### 🎁 다른사람 코드

- 접근 방법은 똑같지만 `pop()` 를 통해서 굳이 다시 해야하지 않을 계산들을 줄였다.

```python
N, K = map(int, input().split())

Coins = []
for i in range(N) : Coins.append(int(input()))


ans = 0
while K > 0 :
    coin = Coins.pop()
    ans += K // coin
    K %= coin

print(ans)
```



![image-20210604102523998](README.assets/image-20210604102523998.png)

