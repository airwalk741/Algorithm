import sys

sys.stdin = open('input (6).txt', 'r')

# 곱해서 최대인 값 찾는 함수
def multi(a, b):

    n = len(a)
    m = len(b)

    result_max = 0
    # 긴 상자의 길이를 벗어나면 안됨 ( m - n + 1 )
    for i in range(m-n+1):
        result = 0
        for j in range(n):
            result += (a[j] * b[i+j])
        if result_max < result:
            result_max = result

    return result_max

T = int(input())

for tc in range(1, T+1):

    n, m = map(int, input().split())

    a = list(map(int, input().split()))

    b = list(map(int, input().split()))


    result = 0
    print('#{}'.format(tc), end=' ')
    if n < m:
        print(multi(a, b))

    else:
        print(multi(b, a))