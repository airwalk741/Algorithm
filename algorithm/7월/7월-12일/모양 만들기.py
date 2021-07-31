import sys
sys.stdin = open('input.txt', 'r')


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]




n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

## 무리 안에 개수 세기 (idx 2부터 시작)
moori = [0, 0]

# 0하고 1은 이미 격자판에 있기 때문
idx = 2


visited = [[0] * m for _ in range(n)]


# 무리 체크하면서 무리 안에 인원수 세기
for i in range(n):
    for j in range(m):
        # 1인거는 처음 들어온 input 값, 방문 안 했다면
        if arr[i][j] == 1 and not visited[i][j]:

            cnt = 1  # 인원 수

            # dfs
            q = [(i, j)]

            while q:

                r, c = q.pop()

                # idx번 무리 (무리마다 번호를 붙인다)
                arr[r][c] = idx

                for k in range(4):
                    x = dr[k] + r
                    y = dc[k] + c
                    if -1 < x < n and -1 < y < m: # 범위
                        if arr[x][y] == 1 and not visited[x][y]: # 방문 안했으면
                            q.append((x, y)) # q에 담고
                            visited[x][y] = 1 # 방문 체크
                            cnt += 1 # 인원수 + 1

            # 무리의 인원 수 담기
            moori.append(cnt)
            # 무리 번호 증가
            idx += 1



result = 0


# 이제 격자판에 0인 것 하나만 1로 바꾸면서 세기
for i in range(n):
    for j in range(m):
        # 0이라면
        if not arr[i][j]:
            # 모양 담을 배열
            moyang = []

            for k in range(4):
                x = dr[k] + i
                y = dc[k] + j
                # 4방향 탐색 하면서 무리 체크하기
                if -1 < x < n and -1 < y < m:
                    if arr[x][y]:
                        # 체크 하지 않은 무리면 담기
                        if arr[x][y] not in moyang:
                            moyang.append(arr[x][y])

            # 인원 수
            res = 0

            # 무리 별 인원 수 더하기
            for idx in moyang:

                res += moori[idx]


            # 최댓값 찾기
            result = max(result, res)


# 0을 1로 바꾼거니까 + 1
print(result + 1)










