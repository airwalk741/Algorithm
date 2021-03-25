import sys

sys.stdin = open('input (43).txt', 'r')


# search => x = 1에서 수열의 규칙 찾기
# 규칙찾고 찾는 숫자와 비교해서 x=1일때 y좌표 대략 찾기
# 찾는 숫자와의 차이에 따라서 x좌표 y좌표 판별하기
  # => x좌표는 차이의 +, y좌표는 차이의 -
  # => 위에서 아래로 좌에서 우로 숫자가 증가하기 때문
def search(number):
    i = 1

    while True:

        if i * (i - 1) > 2 * (number - 1):
            i -= 1
            break
        elif i * (i - 1) == 2 * (number - 1):
            break

        i += 1

    num = int((i * (i - 1)) / 2 + 1)

    x, y = (1 + (number - num)), (i - (number - num))

    return x, y

# search 구했을 때 한 것을 반대로 한다.
def re_search(x, y):

    num1 = x - 1

    num2 = y + num1

    real_num = int(num2 * (num2 - 1) / 2 + 1) + num1

    return real_num


T = int(input())

for tc in range(1, T + 1):
    print('#{}'.format(tc), end=' ')

    p, q = map(int, input().split())

    x1, y1 = search(p)

    x2, y2 = search(q)

    print(re_search(x1+x2, y1+y2))

