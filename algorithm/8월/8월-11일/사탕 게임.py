import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

## 두 개 선택해서 가로로 바꾸면 해당 행에서 최대길이, 두 점의 행에서 열(가로)의 최대 길이 구하기
## 두 개 선택해서 세로로 바꾸면 해당 열에서 최대길이, 두 점의 열에서 행(가로)의 최대 길이 구하기

dr = [0, 1]
dc = [1, 0]

def search(r, c, x, y, dist):
    global result

    ## 처음엔 다 구해서 최댓값 찾기
    if dist == 2:
        for i in range(n):
            cnt_c = 1
            cnt_r = 1
            for j in range(n-1):

                if arr[i][j] == arr[i][j + 1]:
                    cnt_c += 1
                else:
                    if cnt_c > result:
                        result = cnt_c
                    cnt_c = 1

                if arr[j][i] == arr[j + 1][i]:
                    cnt_r += 1
                else:
                    if cnt_r > result:
                        result = cnt_r
                    cnt_r = 1
        result = max(result, cnt_r, cnt_c)

    ## 가로
    elif k == 0:

        cnt_c = 1
        ## 행
        for i in range(n - 1):
            if arr[r][i] == arr[r][i + 1]:
                cnt_c += 1
            else:
                result = max(result, cnt_c)
                cnt_c = 1

        result = max(result, cnt_c)

        ## 열
        cnt_r1 = 1
        cnt_r2 = 1
        for i in range(n - 1):
            if arr[i][c] == arr[i + 1][c]:
                cnt_r1 += 1
            else:
                result = max(result, cnt_r1)
                cnt_r1 = 1

            if arr[i][y] == arr[i + 1][y]:
                cnt_r2 += 1
            else:
                result = max(result, cnt_r2)
                cnt_r2 = 1
        result = max(result, cnt_r1, cnt_r2)

    ## 세로
    else:

        ## 열
        cnt_r = 1

        for i in range(n - 1):
            if arr[i][c] == arr[i + 1][c]:
                cnt_r += 1
            else:
                result = max(result, cnt_r)
                cnt_r = 1


        ## 행
        cnt_c1 = 1
        cnt_c2 = 1

        for i in range(n - 1):

            if arr[r][i] == arr[r][i + 1]:
                cnt_c1 += 1
            else:
                result = max(result, cnt_c1)
                cnt_c1 = 1

            if arr[x][i] == arr[x][i + 1]:
                cnt_c2 += 1
            else:
                result = max(result, cnt_c2)
                cnt_c2 = 1

        result = max(result, cnt_c1, cnt_c2)

n = int(input())

arr = [list(input().rstrip()) for _ in range(n)]

result = 0

search(0, 0, 0, 0, 2)

for i in range(n):
    for j in range(n):

        for k in range(2):
            x = dr[k] + i
            y = dc[k] + j

            if -1 < x < n and -1 < y < n:
                arr[i][j], arr[x][y] = arr[x][y], arr[i][j]
                search(i, j, x, y, k)
                arr[i][j], arr[x][y] = arr[x][y], arr[i][j]

print(result)

