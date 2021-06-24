import sys
sys.stdin = open('input (43).txt', 'r')

baseball = []

for i in range(1, 10):
    for j in range(1, 10):
        if i != j:
            for k in range(1, 10):
                if i != k and j != k:
                    baseball.append(str(i) + str(j) + str(k))

length = len(baseball)

n = int(input())

games = [list(map(int, input().split())) for _ in range(n)]

for game in games:

    ball, s, b = game

    ball = str(ball)

    for i in range(length):
        if baseball[i]:
            check = list(baseball[i])
            s_cnt = 0
            b_cnt = 0

            for j in range(3):
                if ball[j] == check[j]:
                    s_cnt += 1

                if ball[j] in check:
                    b_cnt += 1

            b_cnt -= s_cnt

            if s != s_cnt or b != b_cnt:
                baseball[i] = 0

print(length - baseball.count(0))








