import sys
sys.stdin = open('input (43).txt', 'r')


def winner(r, c, player):

    # 찾으면 가장 왼쪽 바둑볼 위치
    left_r = r
    left_c = c

    # 좌상 우하 대각선
    buttom_cross = 1

    i = 1
    buttom = 1
    above = 1
    while i < 19 and buttom_cross < 6:
        # 우하
        if buttom:
            if 0 < r + i < 19 and 0 < c + i < 19:
                if arr[r + i][c + i] == player:
                    buttom_cross += 1
                else:
                    buttom = 0
            else:
                buttom = 0
        # 좌상
        if above:
            if 0 < r - i < 19 and  0 < c - i < 19:
                if arr[r - i][c - i] == player:
                    buttom_cross += 1
                    left_r = r - i
                    left_c = c - i
                else:
                    above = 0
            else:
                above = 0
        # 좌상 우하가 끝나면 나간다.
        if not above and not buttom:
            break

        i += 1

    if buttom_cross == 5:
        print(arr[r][c])
        print(left_r + 1, left_c + 1)
        return player

    ##########################################
    # 밑으로는 반복

    # 좌하 우상 대각선
    i = 1
    left_r = r
    left_c = c
    above_cross = 1
    buttom = 1
    above = 1
    while i < 19 and above_cross < 6:

        if buttom:
            if 0 < r + i < 19 and 0 < c - i < 19:
                if arr[r + i][c - i] == player:
                    above_cross += 1
                    left_r = r + i
                    left_c = c - i
                else:
                    buttom = 0
            else:
                buttom = 0

        if above:
            if 0 < r - i < 19 and 0 < c + i < 19:
                if arr[r - i][c + i] == player:
                    above_cross += 1
                else:
                    above = 0
            else:
                above = 0

        if not above and not buttom:
            break

        i += 1

    if above_cross == 5:
        print(arr[r][c])
        print(left_r + 1, left_c + 1)
        return player


    # 가로
    width = 1
    i = 1
    left_r = r
    left_c = c
    buttom = 1
    above = 1
    while i < 19 and width < 6:

        if buttom:
            if 0 < r < 19 and 0 < c - i < 19:
                if arr[r][c - i] == player:
                    width += 1
                    left_r = r
                    left_c = c - i
                else:
                    buttom = 0
            else:
                buttom = 0

        if above:
            if 0 < r < 19 and 0 < c + i < 19:
                if arr[r][c + i] == player:
                    width += 1
                else:
                    above = 0
            else:
                above = 0

        if not above and not buttom:
            break

        i += 1

    if width == 5:
        print(arr[r][c])
        print(left_r + 1, left_c + 1)
        return player

    # 세로
    height = 1
    i = 1
    left_r = r
    left_c = c
    buttom = 1
    above = 1
    while i < 19 and height < 6:

        if buttom:
            if 0 < r + i < 19 and 0 < c < 19:
                if arr[r + i][c] == player:
                    height += 1
                else:
                    buttom = 0
            else:
                buttom = 0

        if above:
            if 0 < r - i < 19 and 0 < c < 19:
                if arr[r - i][c] == player:
                    height += 1
                    left_r = r - i
                    left_c = c
                else:
                    above = 0
            else:
                above = 0

        if not above and not buttom:
            break

        i += 1

    if height == 5:
        print(arr[r][c])
        print(left_r + 1, left_c + 1)
        return player


    return 0

arr = [list(map(int, input().split())) for _ in range(19)]

winner_check = 0

for i in range(19):
    for j in range(19):
        if arr[i][j]:
            if winner(i, j, arr[i][j]):
                winner_check = 1
                break
    if winner_check:
        break
else:
    print(0)