import sys
sys.stdin = open('input (9).txt', 'r')

T = int(input())

for tc in range(1, T+1):

    print('#{}'.format(tc), end=' ')

    arr = [list(map(int, input().split())) for _ in range(9)]

    cnt_r = [0] * 10 # 행의 숫자 카운트
    cnt_c = [0] * 10 # 열의 숫자 카운트
    res = 1

    for i in range(9):
        for j in range(9):
            cnt_r[arr[i][j]] += 1
            cnt_c[arr[j][i]] += 1

        # 행, 열이 하나씩 돌때마다 돌때의 횟수가 9의 배수의 개수가 나와야한다.
        # 돌때의 횟수가 9의 배수가 아니면 어떠한 수가 중복으로 나왔다는 것
        if cnt_r.count((i+1)) != 9 or cnt_c.count((i+1)) != 9:
            res = 0
            break

    if res == 0:
        print(res)
        continue

    cnt = [0] * 10
    k = 1
    # 파리 퇴치와 비슷하게 풂풂
    for  in range(0, 9, 3):
        for j in range(0, 9, 3):
            for x in range(3):
                for y in range(3):
                    cnt[arr[x][y]] += 1

            if cnt.count(k) != 9:
                res = 0
                break
            k += 1


    print(res)

