import sys
sys.stdin = open('input (43).txt', 'r')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):
    global result
    cnt = 1 # 연결된 집의 수
    arr[r][c] = 0
    s = [[r, c]]

    while s:
        num = s.pop()

        for i in range(4):
            x = num[0] + dr[i]
            y = num[1] + dc[i]
            if -1 < x < n and -1 < y < n:
                if arr[x][y]:
                    cnt += 1
                    arr[x][y] = 0
                    s.append([x, y])

    result.append(cnt) # 연결된 집 수 결과값에 추가

n = int(input())

arr = [list(map(int, input())) for _ in range(n)]

result = []

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            dfs(i, j) # 집이 있으면 탐색

print(len(result)) # 그룹 수
result.sort() # 연결된 수가 적은 것부터 정렬
for i in result:
    print(i)

