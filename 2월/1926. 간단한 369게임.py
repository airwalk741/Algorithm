import sys

sys.stdin = open('input (6).txt', 'r')

n = int(input())

# 1부터 n까지 369게임
for i in range(1, n+1):
    # count 함수를 이용해서 3, 6, 9가 있는지 확인해서 출력한다.
    if str(i).count('3') + str(i).count('6') + str(i).count('9'):
        print('-'*int(str(i).count('3') + str(i).count('6') + str(i).count('9')), end=' ')
    else:
        print(i, end=' ')
