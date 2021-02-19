import sys

sys.stdin = open('input (6).txt', 'r')

T = int(input())

for tc in range(1, T+1):

    n, q = map(int, input().split())

    result = [0] * n
    count = 1
    # q의 길이만큼 반복
    while q > 0:
        # r, l을 담는다
        r, l = map(int, input().split())
        #  r에서부터 l까지 result를 수정한다.
        for i in range(r-1, l):
            result[i] = count

        count += 1
        q -= 1


    print('#{}'.format(tc), *result)
