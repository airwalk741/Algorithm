import sys

sys.stdin = open('input (43).txt', 'r')

operater = ['+', '-', '*', '/']

def dfs(num, idx):
    global result_min
    global result_max


    if idx == n-1:
        if num > result_max:
            result_max = num
        if num < result_min:
            result_min = num
        # print('값 : ',  num)
        return

    for i in range(4):
        if operater_num[i] != 0:
            if i == 0:
                num = num + number[idx]
            elif i == 1:
                num = num - number[idx]
            elif i == 2:
                num = num * number[idx]
            elif i == 3:
                num = -abs(num // number[idx])

            operater_num[i] -= 1
            dfs(num, idx+1)
            operater_num[i] += 1



T = int(input())

for tc in range(1, 1+T):

    n = int(input())

    operater_num = list(map(int, input().split()))

    number = list(map(int, input().split()))

    result_max = -987654321
    result_min = 987654321

    dfs(number[0], 1)

    print(result_max - result_min)