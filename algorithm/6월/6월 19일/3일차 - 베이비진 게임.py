import sys
sys.stdin = open('input (43).txt', 'r')

def triple(arr):

    for i in range(8):
        if arr[i] and arr[i+1] and arr[i+2]:
            return 1




T = int(input())

for tc in range(1, T+1):

    print('#{}'.format(tc), end=' ')

    cards = list(map(int, input().split()))

    player1 = [0] * 10
    player2 = [0] * 10
    check = 0

    for i in range(12):

        if i % 2:
            player2[cards[i]] += 1

            if player2[cards[i]] == 3 or triple(player2):
                print(2)
                break

        else:

            player1[cards[i]] += 1

            if player1[cards[i]] == 3 or triple(player1):
                print(1)
                break
    else:
        print(0)


