import sys
sys.stdin = open('input (43).txt', 'r')
from collections import deque
import pprint

dr = [-1, -1, 0, 1, 1, 1, 0, -1, 0]
dc = [0, 1, 1, 1, 0, -1, -1, -1, 0]


def search():
    global cnt

    q = deque()
    q.append((0, 0))

    first = 1

    while q:

        length = len(q)

        if not first:

            for i in range(8):
                # 왼쪽 열 없애고
                # 오른쪽에 열 추가
                ch = game[i].pop(0)
                game[i].append(0)

                if ch == '#':
                    cnt -= 1

        # '#'이 없으면 목적지까지 도착 가능
        if cnt == 0:
            return 1


        for _ in range(length):

            r, c = q.popleft()
            # 벽이면 이동 x
            if game[r][c] == '#':
                continue

            # 9개 방향
            for i in range(9):
                x = dr[i] + r
                y = dc[i] + c

                if -1 < x < 8 and -1 < y < 8:
                    if game[x][y] != '#':
                        q.append((x, y))

        first = 0

    return 0




arr = [list(input()) for _ in range(8)]

game = [[0] * 8 for _ in range(8)]

cnt = 0

# 오른쪽으로 돌리기
for i in range(8):
    for j in range(8):
        if arr[i][j] == '#':
            cnt += 1

        arr[i][j], game[j][7 - i] = game[j][7 - i], arr[i][j]


# pprint.pprint(game)
print(search())

