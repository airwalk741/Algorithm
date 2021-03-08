import sys

sys.stdin = open('input (43).txt', 'r')

def _max(idx, num):
    global result

    # 바꾼 횟수와 동일했을 때 빠져나오는  if문
    if idx == int(change):
        nun = ''
        for k in num:
            nun += str(k)
        if int(nun) > result:
            result = int(nun)

        return

    # 왼쪽이 오른쪽보다 작으면 바꿀 필요가 없음
    # 오른쪽이 크면 바꿔서 깊이우선 탐색
    # 모든 바꾸는 경우의 수를 찾아서 큰 값을 찾을 것
    for i in range(len(num)):
        for j in range(i, len(num)):
            if i != j:
                if num[i] <= num[j]:
                    num[i], num[j] = num[j], num[i]
                    _max(idx+1, num)
                    num[i], num[j] = num[j], num[i]

T = int(input())

for tc in range(1, T+1):

    num, change = input().split()

    number = []
    for i in num:
        number.append(int(i))

    result = 0

    _max(0, number)

    print('#{}'.format(tc), end=' ')
    print(result)
