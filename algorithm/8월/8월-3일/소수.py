import sys
sys.stdin = open('input.txt', 'r')



m = int(input())
n = int(input())


arr = [1] * (n + 1)

arr[0], arr[1] = 0, 0

_sum = 0
_min = 0


## 에라토스테네스의 체
for i in range(2, n+1):

    if arr[i]:

        if i >= m:
            if not _min: ## 최소값의 변화가 없었으면 최솟값으로
                _min = i

            _sum += i ## m 과 n 사이 ㅗ수 더하기

        for j in range(2, n + 1):

            if i * j >= n + 1:
                break

            arr[i * j] = 0

## 최소, 합이 0이라면 소수 없는 것
if not _min and not _sum:
    print(-1)
else:
    print(_sum)
    print(_min)
