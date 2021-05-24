import sys
sys.stdin = open('input (43).txt', 'r')


T = int(input())

for tc in range(1, 1 + T):
    print('#{}'.format(tc), end=' ')
    n, k = map(int, input().split())

    arr = []

    for i in range(n):
        x, y, z = map(int, input().split())
        # 계산해서 넣기
        arr.append(round(x*0.35 + y*0.45 + z*0.2, 3))

    result = arr[k-1]
    # 정렬
    arr.sort(reverse=True)

    result = ((arr.index(result) + 1 ) / n) * 10
    # print(result)

    if 0 <= result <= 1:
        print('A+')
    elif 1 < result <= 2:
        print('A0')
    elif 2 < result <= 3:
        print('A-')
    elif 3 < result <= 4:
        print('B+')
    elif 4 < result <= 5:
        print('B0')
    elif 5 < result <= 6:
        print('B-')
    elif 6 < result <= 7:
        print('C+')
    elif 7 < result <= 8:
        print('C0')
    elif 8 < result <= 9:
        print('C-')
    elif 9 < result <= 10:
        print('D0')



