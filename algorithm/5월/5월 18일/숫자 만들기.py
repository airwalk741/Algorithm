import sys
sys.stdin = open('input (43).txt', 'r')

# 사칙연산 함수
def operation(num1, num2, oper):

    if oper == 0:
        return num1 + num2
    elif oper == 1:
        return num1 - num2
    elif oper == 2:
        return num1 * num2
    elif oper == 3:
        return int(num1 / num2)

# 순열
# idx: 연산자 배열 인덱스 , result: 연산된 값
def perm(idx, result):
    global _min
    global _max

    # 연산의 개수와 idx와 같을 때 최소, 최대 구하기
    if idx == n - 1:

        _max = max(result, _max)
        _min = min(result, _min)


    else:
        for i in range(4):

            if operater[i]:

                operater[i] -= 1 # 사용 체크

                if idx == 0: # 처음에는 첫번째 숫자와 두번째 숫자 계산
                    next_num = operation(numbers[idx], numbers[idx+1], i)
                    perm(idx+1, next_num)

                else: # 이후부터는 연산된 숫자와 그 다음 숫자 계산
                    next_num = operation(result, numbers[idx+1], i)
                    perm(idx+1, next_num)

                operater[i] += 1 # 사용 복구


T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')

    n = int(input())
    # 연산자 모음
    operater = list(map(int, input().split()))
    # 숫자모음
    numbers = list(map(int, input().split()))

    _max = -987654321
    _min = 987654321

    perm(0, 0)


    # while operater_idx:
    #
    #     operate = operater_idx.pop()
    #
    #     result = operation(numbers[0], numbers[1], operate[0])
    #
    #     for i in range(1, len(operate)):
    #         result = operation(result, numbers[i+1], operate[i])
    #
    #
    #     _max = max(result, _max)
    #     _min = min(result, _min)


    print(_max - _min)








