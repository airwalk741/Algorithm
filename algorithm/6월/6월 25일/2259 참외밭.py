import sys
sys.stdin = open('input (43).txt', 'r')

fruit = int(input())

board = []

r_max = 0
c_max = 0

for _ in range(6):

    dist, width = map(int, input().split())
    if dist in [1, 2]:
        c_max = max(c_max, width)
    else:
        r_max = max(r_max, width)
    board.append(width)


yes_board = []
no_board = []

for i in range(6):

    ch = 0

    if board[i] != c_max and board != r_max:
        if i + 1 > 5:
            j = -1
        else:
            j = i
        if board[j + 1] != c_max and board[j + 1] != r_max:
            ch += 1
        if i - 1 < 0:
            j = 6
        else:
            j = i
        if board[j - 1] != c_max and board[j - 1] != r_max:
            ch += 1

    if ch == 2:
        no_board.append(board[i])



result = r_max * c_max - no_board[0] * no_board[1]

print(result * fruit)













