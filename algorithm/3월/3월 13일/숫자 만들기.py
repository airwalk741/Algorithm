import sys

sys.stdin = open('input (43).txt', 'r')

# 연산 하는 함수
def operation(a, b, operater_num):

    if operater_num == 0:
        return a + b
    elif operater_num == 1:
        return a - b
    elif operater_num == 2:
        return a * b
    elif operater_num == 3:
        return int(a / b)


def dfs(idx, num):
    global result_max
    global result_min

    # 연산자의 개수가 없으면 최댓값 최소값을 비교하여 저장한다
    if sum(operater_num) == 0:
        if num > result_max:
            result_max = num
        if num < result_min:
            result_min = num
        return

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


T = int(input())

for tc in range(1, T+1):

    n = int(input())

    operater_num = list(map(int, input().split()))

    number = list(map(int, input().split()))

    result_max = -987654321
    result_min = 987654321

    dfs(1, number[0])
    print('#{}'.format(tc), end=' ')
    print(result_max-result_min)