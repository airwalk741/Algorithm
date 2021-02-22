import sys
sys.stdin = open('input (3).txt', 'r')


T = int(input())

for tc in range(1, T+1):

    print('#{}'.format(tc), end=' ')
    n = int(input())

    board = [input() for _ in range(n)]

    result = 'NO' # 오목이 나오지 않으면 NO 출력

    for i in range(n):
        count_row = 0 # 가로 오목 확인
        count_col = 0 # 세로 오목 확인
        for j in range(n):
            # 돌이 있으면
            if board[i][j] == 'o':
                count_row += 1
                # 오목이 판정이 되면 break
                if count_row == 5:
                    result = 'YES'
                    break
            else: # 돌이 없으면 다시 0으로
                count_row = 0
            # 돌이 있으면
            if board[j][i] == 'o':
                count_col += 1
                # 오목이 판정이 되면
                if count_col == 5:
                    result = 'YES'
                    break
            else: # 돌이 없으면 0
                count_col = 0
        if result == 'YES':
            break

    for i in range(n - 5 + 1):
        for j in range(n - 5 + 1):
            count_cross = 0  # 대각선 오목 확인
            count_re_cross = 0  # 반대 대각전 오목 확인
            for k in range(5):
                # 좌상에서 우하인 대각선에서 오목 찾기
                if board[i+k][j+k] == 'o':
                    count_cross += 1
                    if count_cross == 5:
                        result = 'YES'
                        break
                else:
                    count_cross = 0
                # 좌하에서 우상인 대각선에서 오목 찾기
                if board[i + k][j - k + 4] == 'o':
                    count_re_cross += 1
                    if count_re_cross == 5:
                        result = 'YES'
                        break
                else:
                    count_re_cross = 0

            if result == 'YES':
                break
        if result == 'YES':
            break

    print(result)












