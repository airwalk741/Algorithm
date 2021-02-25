import sys
sys.stdin = open('input (9).txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    print('#{}'.format(tc), end=' ')
    n = int(input())

    room = []
    my_room = []

    for i in range(n):
        a, b = map(int, input().split())
        room += [a]
        my_room += [b]

    count = [0] * 201

    for i in range(n):
        if room[i] > my_room[i]:
            for j in range((my_room[i]+1)//2, (room[i]+1)//2+1):
                count[j] += 1
        else:
            for j in range((room[i]+1)//2, (my_room[i]+1)//2+1):
                count[j] += 1

    print(max(count))





