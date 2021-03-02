
T = int(input())
for tc in range(1, T+1):
    # 제곱하면 1의 자리 숫자가 반복됨
    number = {
        '1': [1],
        '2': [2, 4, 8, 6],
        '3': [3, 9, 7, 1],
        '4': [4, 6],
        '5': [5],
        '6': [6],
        '7': [7, 9, 3, 1],
        '8': [8, 4, 2, 6],
        '9': [9, 1],

    }

    a, b = map(str, input().split())
    # 만약 a가 10의 배수라면 10출력
    if int(a) % 10 == 0:
        print('10')
    else:

        result = number[str(int(a)%10)]
        print(result[int(b)%(len(result))-1])