# 4 3 2 1 0
#     2 1 0
# 숫자가 2개씩 있으면 2 ** n
# 한개씩 있다면 결과값에 그냥 곱하기 2
   #  2 * n ( 아님 )
n = int(input())

tall = list(map(int, input().split()))

big = max(tall)

# 숫자 개수를 담기 위한 딕셔너리
ani = {}

for i in range(big+1):
    ani[i] = 0

for i in tall:
    ani[i] += 1

i = 0
result = 1
cnt = 0 # 숫자가 두개씩 있는지 없는지 확인하는 것 ( 1 이상이라면 한개 있는 것)
cnt_p = 0 # 숫자 중간에 0이 있는지 확인하는 것
          # ex) 2
          #     0 2 들어왔을 때

for i in range(big+1):

    if ani[i] == 0: # 숫자 없으면 ( 끝났다고 인식 )
        cnt_p = 1  # 끝남을 알려줌
        if cnt != 0: # cnt가 계속 증가 했으니 계속 1개씩 있었다고 인식하는 거임
            result *= 2
            cnt = 0 # 다시 0으로 바꿔줌 나중에 또 ani[i]가 0이라면 끝남으로 인식하기 위해
        else: # cnt가 0이면 끝
            print('0')
            break
    elif ani[i] == 1: # 숫자가 1개라면
        if cnt_p != 0: # 숫자들 중간에 개수가 0인 것이 나왔다는 것
            print('0')
            break
        cnt += 1
    elif ani[i] == 2: # 숫자가 2개라면 2의 제곱승 만큼 결과 증가
        if cnt_p != 0:
            print('0')
            break
        if cnt == 0:
            result *= 2
        else:
            print('0')
            break
    else: # 토끼 고양이 두 종류인데 그것보다 많은 숫자 가지면 안댐
        print('0')
        break
else:
    if cnt != 0:
        result *= 2
    print(result)




