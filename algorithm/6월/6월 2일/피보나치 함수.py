import sys
sys.stdin = open('input (43).txt', 'r')


T = int(input())

for _ in range(T):

    n = int(input())

    zero_visited = [0] * 41
    zero_visited[0], zero_visited[1] = 1, 0

    one_visited = [0] * 41
    one_visited[0], one_visited[1] = 0, 1

    if n >= 2:
        for i in range(2, 41):
            zero_visited[i] = zero_visited[i-1] + zero_visited[i-2]


        for i in range(2, 41):
            one_visited[i] = one_visited[i - 1] + one_visited[i - 2]


    print(zero_visited[n], one_visited[n])



