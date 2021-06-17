import sys
sys.stdin = open('input (43).txt', 'r')


while True:

    try:
        a, n, b = input().split()

        # 10진수 변환
        num = int(n, int(a))

        result = ''
        b = int(b)

        # b진수 변환
        while num:

            res = num % b

            if res > 9:
                res = chr(res + 55)
                result += res
            else:
                result += str(res)

            num = num // b

        # 거꾸로 출력하기
        for i in range(len(result)-1, -1, -1):
            print(result[i], end='')

        # 빈값이면 while문 입장한게 아니기 때문에 0
        if not result:
            print(0, end='')

        print()


    except:
        break

