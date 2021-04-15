import sys
sys.stdin = open('input (43).txt', 'r')

def check(arr):

    if 3 in arr: # 트리플 체크
        return 1

    for i in range(8): # 런 체크
        if arr[i] and arr[i+1] and arr[i+2]:
            return 1

T = int(input())

for tc in range(1, 1+T):
    print('#{}'.format(tc), end=' ')

    card = list(map(int, input().split()))

    player1 = [0] * 10
    player2 = [0] * 10

    result = 0

    for i in range(0, 11, 2):
        player1[card[i]] += 1
        if i >= 4:
            if check(player1):
                result = 1
                break
        player2[card[i+1]] += 1

        if i >= 4:
            if check(player2):
                result = 2
                break


    print(result)

