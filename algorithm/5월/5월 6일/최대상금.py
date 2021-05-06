import sys
from collections import deque
sys.stdin = open('input (43).txt', 'r')

def dfs(idx, cnt):
    global result

    if cnt:
        if money == max_money: # 최댓값과 같고 바꿀 수 있는 기회가 있으면
            ch = 0
            for i in range(len(money)-1): # money에 같은 숫자가 있는지 판별
                if money[i] == money[i+1]:
                    ch = 1 # 같은 숫자가 있음을 체크
                    break

            if ch == 0: # 같은 숫자가 없으면 최대 상금이므로 1의 자리와 10의 자리를 남은 교체 횟수만큼 바꿔준다.
                while cnt:
                    money[-1], money[-2] = money[-2], money[-1]
                    cnt -= 1

            fake_result = int(''.join(money)) # 결과로 나온 상금

            if result < fake_result: # result에 저장한 상금 보다 크면
                result = fake_result
            return

        else:
            # 아직 최댓값과 같지 않으면
            for i in range(idx, len(money) - 1): # idx-1 자리는 이미 교체를 완료해서 큰 숫자를 저장했으므로 idx 자리부터 시작
                for j in range(i, len(money)): # idx 다음 자리부터 비교해서
                    if int(money[i]) < int(money[j]): # idx 다음자리의 숫자가 크다면
                        money[i], money[j] = money[j], money[i] # 교환 해주고
                        dfs(idx + 1, cnt - 1) # idx 다음자리인 idx+1 하고 교체해줬으므로 cnt - 1
                        money[i], money[j] = money[j], money[i] # 원상 복구

    else: # 교체 횟수 없으면 result와 비교

        fake_result = int(''.join(money))
        if result < fake_result:
            result = fake_result
        return



T = int(input())

for tc in range(1, 1+T):

    print('#{}'.format(tc), end=' ')
    money, change = input().split()

    money = list(money)
    change = int(change)

    max_money = sorted(money, reverse=True) # money의 최댓값
    result = 0

    dfs(0, change)

    print(result)



