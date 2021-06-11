import sys
sys.stdin = open('input (43).txt', 'r')


for _ in range(10):


    num = int(input())

    if num == 0:
        break

    result = 0 # 뒤로
    res = 0 # 합

    while num:

        n = num % 10

        result = result * 10 + n
        res += n

        num = num // 10

    print(result, res)






