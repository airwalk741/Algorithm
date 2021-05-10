import sys
sys.stdin = open('input (43).txt', 'r')

# 행 시작, 행 끝, 열 시작, 열 끝
def seach(r_start, r_end, c_start, c_end):
    global blue, white

    now = arr[r_start][c_start] # 현재 지점 색

    for i in range(r_start, r_end):
        for j in range(c_start, c_end):

            if arr[i][j] != now: # 색이 다르면 4등분으로 자르기
                seach(r_start, (r_start+r_end)//2, c_start, (c_start+c_end)//2)
                seach((r_start+r_end)//2, r_end, c_start, (c_start+c_end)//2)
                seach(r_start, (r_start+r_end)//2, (c_start+c_end)//2, c_end)
                seach((r_start+r_end)//2, r_end, (c_start+c_end)//2, c_end)
                return
    if now:
        blue += 1
    else:
        white += 1


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

blue, white = 0, 0

seach(0, n, 0, n)

print(white)
print(blue)



















