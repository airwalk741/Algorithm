import sys
sys.stdin = open('input (9).txt', 'r')

T = int(input())

for tc in range(1, T+1):

    n = int(input())
    print('#{}'.format(tc))
    # n이 1이거나 2일때 실행
    if n < 3:
        for i in range(1,n+1):
            print('1 '*i)
    # n이 2이상일때
    if n > 2:
        for i in range(2, n+1):
            # n이 1이거나 2일때 출력한거 출력
            # 1
            # 1 1
            if i < 3:
                for k in range(1, i+1):
                    print('1 ' * k)
            # 그게 아니라면 1 사이에 n-1의 숫자만큼 쓴다
            # 1
            # 1 2 1
            else:
                print('1',end=' ')
                print('{} '.format(i-1)*(i-2), end='')
                print('1')

