import sys
sys.stdin = open('input (9).txt', 'r')


T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())

    arr = [[0] * (n+1) for _ in range(n+1)]

    c = []
    r = []
    coin = []

    for i in range(m):
        x, y, z = map(int, input().split())
        c += [x]
        r += [y]
        coin += [z]

    for i in range(n//2 - 1, n//2 + 1):
        for j in range(n//2 - 1, n//2 + 1):
            if i == j:
                arr[i+1][j+1] = 2
            else:
                arr[i+1][j+1] = 1


    for i in range(m):
        arr[r[i]][c[i]] = coin[i]

        # 가로 오른쪽
        j = 0
        change = c[i]
        while c[i] + j <= n:

            if arr[r[i]][c[i]+j] == coin[i]:
                change = c[i] + j
            elif arr[r[i]][c[i]+j] == 0:
                break
            j += 1

        for k in range(c[i], change+1):
            arr[r[i]][k] = coin[i]

        # 가로 왼쪽
        j = 0
        change = c[i]

        while c[i] - j >= 0:

            if arr[r[i]][c[i]-j] == coin[i]:
                change = c[i] - j
            elif arr[r[i]][c[i]-j] == 0:
                break

            j += 1

        for k in range(change, c[i]):
            arr[r[i]][k] = coin[i]

        # 좌상 우하
        j = 0
        change_r = r[i]
        change_c = c[i]
        while r[i] + j <= n and c[i] + j <= n:

            if arr[r[i]+j][c[i]+j] == coin[i]:
                change_r = r[i] + j
                change_c = c[i] + j
            elif arr[r[i] + j][c[i] + j] == 0:
                break

            j += 1

        x = 0
        while r[i] + x <= n and c[i] + x <= n:


            if r[i] + x == change_r:
                if c[i] + x == change_c:
                    break
            arr[r[i] + x][c[i] + x] = coin[i]
            x += 1

        # 우하 좌상
        j = 0
        change_r = r[i]
        change_c = c[i]
        while r[i] + j <= n and c[i] - j > 0:

            if arr[r[i] + j][c[i] - j] == coin[i]:
                change_r = r[i] + j
                change_c = c[i] - j
            elif arr[r[i] + j][c[i] - j] == 0:
                break

            j += 1

        x = 0
        while r[i] + x <= n and c[i] - x > 0:


            if r[i] + x == change_r:
                if c[i] - x == change_c:
                    break
            arr[r[i] + x][c[i] - x] = coin[i]
            x += 1

        #우상 좌하
        j = 0
        change_r = r[i]
        change_c = c[i]
        while r[i] - j > 0 and c[i] - j > 0:
            result = arr[r[i] - j][c[i] - j]
            if arr[r[i] - j][c[i] - j] == coin[i]:
                change_r = r[i] - j
                change_c = c[i] - j
            elif arr[r[i] - j][c[i] - j] == 0:
                break

            j += 1

        x = 0
        while r[i] - x > 0 and c[i] - x > 0:

            if r[i] - x == change_r: ##dlrj
                if c[i] - x == change_c:
                    break

            arr[r[i] - x][c[i] - x] = coin[i]
            x += 1

        # 좌하 우상
        j = 0
        change_r = r[i]
        change_c = c[i]
        while r[i] - j > 0 and c[i] + j <= n:

            if arr[r[i] - j][c[i] + j] == coin[i]:
                change_r = r[i] - j
                change_c = c[i] + j
            elif arr[r[i] - j][c[i] + j] == 0:
                break

            j += 1

        while r[i] - x > 0 and c[i] + x <= n:


            if r[i] - x == change_r:
                if c[i] + x == change_c:
                    break
            arr[r[i] - x][c[i] + x] = coin[i]
            x += 1

        # 아래쪽
        j = 0
        change = r[i]
        while r[i] + j <= n:

            if arr[r[i]+j][c[i]] == coin[i]:
                change = r[i] + j
            elif arr[r[i]+j][c[i]] == 0:
                break

            j += 1

        for k in range(r[i], change + 1):
            arr[k][c[i]] = coin[i]

        ##
        ## 위쪽
        j = 0
        change = r[i]
        while r[i] - j > 0:

            if arr[r[i] - j][c[i]] == coin[i]:
                change = r[i] - j
            elif arr[r[i] - j][c[i]] == 0:
                break

            j += 1

        for k in range(change, r[i]):
            arr[k][c[i]] = coin[i]

    count_a = 0
    count_b = 0

    for i in range(n+1):
        for j in range(n+1):
            if arr[i][j] == 1:
                count_a += 1
            elif arr[i][j] == 2:
                count_b += 1
    print('#{} {} {}'.format(tc, count_a, count_b))













