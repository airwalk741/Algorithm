import sys
from collections import deque
sys.stdin = open('input (43).txt', 'r')
input = sys.stdin.readline
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 치츠가 없는 곳에서( (0,0)지점) 테두리에서 bfs를 돌건데
# 1을 만나면 테두리 치즈이기 때문에 다음에 bfs를 돌때는 테두리 치즈가 사각형 모양의 판의 테두리가 된다.
# 그래서 next_visited 변두에 담아두어 다음 bfs를 돌때는 이것을 사용한다.

def bfs(q):
    global _sum
    global last
    global time

    time += 1
    cnt = 0

    next_visited = []
    while q:
        num = q.popleft()

        for i in range(4):
            x = num[0] + dr[i]
            y = num[1] + dc[i]

            if -1 < x < n + 2 and -1 < y < m + 2 and visited[x][y] == 0:
                # 0이라면 치즈가 없는 빈 곳
                if arr[x][y] == 0:
                    q.append((x, y))
                    visited[x][y] = 1
                # 1이라면 테두리 치즈이기떄문에 시간, 치즈 양을 체크한다.
                elif arr[x][y] == 1:
                    arr[x][y] = 0
                    cnt += 1
                    _sum += 1
                    next_visited.append((x, y))
                    visited[x][y] = 1

    last = cnt # 마지막 bfs였다면 last는 마지막 치즈의 양이다.

    return next_visited


n, m = map(int, input().split())

# 테두리까지 전부 0으로 만들어 준다. ( 0, 0 ) 부터 탐색할건데
# 그냥 입력을 받으면 (0, 0)에도 치즈가 있을 확률이 있기 떄문
# 샘플 테케에는 (0, 0)에 치즈 없는거 같음 ( 그냥 만들어도 pass)

arr = [[0] * (m+2)]

arr += [[0] + list(map(int, input().split())) + [0] for _ in range(n)]

arr += [[0] * (m+2)]

cnt_1 = 0
# 치즈의 개수 세기
for i in range(n+2):
    for j in range(m+2):
        if arr[i][j] == 1:
            cnt_1 += 1

# 한시간 전 출력 하는 것
result = 0

# 치즈가 다 녹았는지 체크하는 것
_sum = 0

# 시간 체크
time = 0

# 방문체크
visited = [[0] *(m+2) for _ in range(n+2)]

q = deque()
q.append((0, 0)) # (0, 0)부터 체크
visited[0][0] = 1 # 방문 체크

while cnt_1 != _sum:

    q = deque((bfs(q)))


print(time)
print(last)

