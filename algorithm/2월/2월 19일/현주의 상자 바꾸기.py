import sys

sys.stdin = open('input (6).txt', 'r')

T = int(input())

for tc in range(1, T+1):

    n, q = map(int, input().split())
    # r, l을 2차원 배열로 선언
    change = [list(map(int, input().split())) for _ in range(q)]
    # 인덱스는 0부터 시작하는 것이여서 한개 더 만들어줌
    result = [0] * (n+1)
    # 1부터 시작해서 들어온 r, l에 따라 result를 바꾼다
    for i in range(len(change)):
        for j in range(change[i][0], change[i][1]+1):
            result[j] = i+1

    print('#{}'.format(tc), end=' ')
    for i in range(1, len(result)):
        print(result[i], end=' ')

    print()

