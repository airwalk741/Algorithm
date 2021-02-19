import sys

sys.stdin = open('input (6).txt', 'r')

T = int(input())

for tc in range(1, T+1):

    n = int(input())
    # 정류장 5000개
    count = [0] * 5001

    while n > 0:
        # 정류장 노선 받아온다
        a, b = map(int, input().split())
        # 정류장에 버스가 몇개 지나가는지 체크하는 것
        for i in range(a, b+1):
            count[i] += 1
        n -= 1

    # 찾고자하는 정류장을 c에 리스트 형태로 담는다
    c =[]
    p = int(input())
    for i in range(p):
        c += [int(input())]


    print('#{}'.format(tc), end=' ')
    for i in range(p):
        print(count[c[i]], end=' ')
    print()