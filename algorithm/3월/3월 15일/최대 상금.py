import sys

sys.stdin = open('input (43).txt', 'r')


def max_money(index, number):
    global result

    change1 = change
    if index == len(number)-1 or index == change1:
        # 이미 최대인 값이기 때문에 교환 횟수가 남아있으면 뒤에 두숫자를
        # 남은 횟수만큼 바꿔준다.
        while index < change1:
            number[-1], number[-2] = number[-2], number[-1]
            change1 -= 1

        number3 = int(''.join(number))
        if result < number3:
            result = number3
        return

    for i in range(index, len(number)):
        for j in range(i+1, len(number)):
            # 되돌아올 변수
            number2 = list(number)

            number[i], number[j] = number[j], number[i]
            max_money(index + 1, number)

            # 되돌아오기
            number = list(number2)

T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc),end=' ')
    num, change = input().split()
    change = int(change)
    number = []

    for i in num:
        number.append(i)

    result = 0

    max_money(0, number)


    print(result)


