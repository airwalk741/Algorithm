import sys
sys.stdin = open('input (43).txt', 'r')

## 좌우로 퍼져 나가기
## 퍼져나가면서 바둑돌 개수 체크
## 왼쪽은 계속 리스트 담아두기

def win(r, c, num):


    ## 가로
    garo = 0
    garo_cnt = 0
    left = 0
    right = 0
    for i in range(1, 19):

        if not right:
            if -1 < c + i < 19:
                if arr[r][c + i] == num:
                    garo_cnt += 1
                else:
                    right += 1

        if not left:
            if -1 < c - i < 19:
                if arr[r][c - i] == num:
                    garo_cnt += 1
                    garo = [r, c - i]
                else:
                    left += 1

        if left and right:
            break


    if garo_cnt == 4:
       return garo



    ## 세로
    garo = 0
    garo_cnt = 0
    left = 0
    right = 0
    for i in range(1, 19):

        if not right:
            if -1 < r + i < 19:
                if arr[r + i][c] == num:
                    garo_cnt += 1
                else:
                    right += 1

        if not left:
            if -1 < r - i < 19:
                if arr[r - i][c] == num:
                    garo_cnt += 1
                    garo = [r - i, c]
                else:
                    left += 1

        if left and right:
            break


    if garo_cnt == 4:
       return garo

    ## 좌상 우하
    garo = 0
    garo_cnt = 0
    left = 0
    right = 0
    for i in range(1, 19):

        if not right:
            if -1 < r + i < 19 and -1 < c + i < 19:
                if arr[r + i][c + i] == num:
                    garo_cnt += 1
                else:
                    right += 1

        if not left:
            if -1 < r - i < 19 and -1 < c - i < 19:
                if arr[r - i][c - i] == num:
                    garo_cnt += 1
                    garo = [r - i, c - i]
                else:
                    left += 1


        if left and right:
            break

    if garo_cnt == 4:
       return garo

    ## 좌하 우상
    garo = 0
    garo_cnt = 0
    left = 0
    right = 0
    for i in range(1, 19):

        if not right:
            if -1 < r - i < 19 and -1 < c + i < 19:
                if arr[r - i][c + i] == num:
                    garo_cnt += 1
                else:
                    right += 1

        if not left:
            if -1 < r + i < 19 and -1 < c - i < 19:
                if arr[r + i][c - i] == num:
                    garo_cnt += 1
                    garo = [r + i, c - i]
                else:
                    left += 1

        if left and right:
            break

    if garo_cnt == 4:
       return garo

    return 0


arr = [list(map(int, input().split())) for _ in range(19)]

result = 0
win_result = 0

for i in range(19):
    for j in range(19):

        if arr[i][j]:
            result = win(i, j, arr[i][j])

            if result:
                win_result = arr[i][j]
                break

    if result:
        break


if result:
    print(win_result)
    print(result[0] + 1, result[1] + 1)
else:
    print(0)

