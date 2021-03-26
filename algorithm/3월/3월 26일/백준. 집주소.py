
while True:

    result = 2 # 맨앞과 맨끝 공백
    num = list(input())

    # 간판 종료
    if len(num) == 1:
        if num[0] == '0':
            break

    # 숫자 사이의 공간
    result += len(num) - 1

    # 숫자에 따라 차지하는 공백
    for i in range(len(num)):
        if num[i] == '0':
            result += 4
        elif num[i] == '1':
            result += 2
        else:
            result += 3

    print(result)