import sys
sys.stdin = open('input (43).txt', 'r')

def cross():

    r_cross = 0
    l_cross = 0
    for i in range(5):
        for j in range(5):
            if i == j:
                r_cross += board[i][j]
            if i + j == 4:
                l_cross += board[i][j]


    if r_cross and l_cross:
        return 0
    elif not r_cross and not l_cross:
        return 2
    else:
        return 1


def search(r, c):

    r_sum = sum(board[r])

    c_sum = 0
    for i in range(5):
        c_sum += board[i][c]

    if r_sum and c_sum:
        return 0
    elif not r_sum and not c_sum:
        if r not in row and c not in colunm:
            row.append(r)
            colunm.append(c)
            return 2
    elif not r_sum:
        if r not in row:
            row.append(r)
            return 1
    elif not c_sum:
        if c not in colunm:
            colunm.append(c)
            return 1


board = [list(map(int, input().split())) for _ in range(5)]

nums = [list(map(int, input().split())) for _ in range(5)]

check = 0

row = []
colunm = []

cnt = 0
bingo = 0

for i in range(5):
    for j in range(5):
        cnt += 1
        for k in range(5):
            if nums[i][j] in board[k]:
                idx = board[k].index(nums[i][j])
                board[k][idx] = 0
                break

        cross_check = cross()

        bingo += cross_check

        bingo += search(k, idx)

        if bingo > 2:
            break
        else:
            bingo -= cross_check
    if bingo > 2:
        break

print(cnt)
















