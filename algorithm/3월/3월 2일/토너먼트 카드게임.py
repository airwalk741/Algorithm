import sys

sys.stdin = open('input (43).txt', 'r')


# 숫자 1은 가위, 2는 바위, 3은 보를 나타낸다.

# 가위바위보 ( 비기면 앞에 있는것이 이김)
def game(a, b):
    if arr[a] == 1:
        if arr[b] == 2:
            return b
    elif arr[a] == 2:
        if arr[b] == 3:
            return b
    elif arr[a] == 3:
        if arr[b] == 1:
            return b
    return a

# 토너먼트
def team(start, end):
    # 재귀함수 끝내는 if
    if start == end:
        return start

    else:
        # 문제에서 왼쪽 부분과 오른쪽 부분 나누는거 써져있음
        # 재귀함수를 이용해서 끝까지 내려간다(가지처럼)
        s = team(start, (start + end) // 2)
        e = team((start + end) // 2 + 1, end)

        return game(s, e)

T = int(input())

for tc in range(1, T + 1):
    print('#{}'.format(tc), end=' ')
    n = int(input())

    arr = list(map(int, input().split()))

    print(team(0, n - 1) + 1)
