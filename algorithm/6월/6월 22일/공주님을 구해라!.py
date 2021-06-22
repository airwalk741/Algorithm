import sys
sys.stdin = open('input (43).txt', 'r')
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(r, c, sword):
    global t

    q = deque()
    q.append((r, c, sword))
    sword_check = 0 # 검을 얻었는지 얻지 못했는지
    while q:

        length = len(q)
        t -= 1 # 시간
        # 음수면 공주 찾지 못한 것
        if t < 0:
            print('Fail')
            return
        # q에 있는 길이 만큼 이동하기
        for _ in range(length):

            r, c, sword = q.popleft()

            for i in range(4):
                x = r + dr[i]
                y = c + dc[i]

                # 공주 위치면 시간 출력하기
                if (x, y) == (n-1, m-1):
                    print(T - t)
                    return

                if -1 < x < n and -1 < y < m:
                    # 검을 가지고 있으면
                    if sword == 2:
                        # visited2는 검을 가지고 있을 때의 방문체크 리스트이다.
                        if not visited2[x][y]:
                            visited2[x][y] = 1
                            q.append((x, y, 2))
                    # 검을 가지고 있지 않으면
                    else:
                        # 길이라면
                        if arr[x][y] == 0:
                            if not visited[x][y]:
                                visited[x][y] = 1
                                q.append((x, y, arr[x][y]))
                        # 검을 얻지 못했을 때
                        if not sword_check:
                            # 검을 찾으면
                            if arr[x][y] == 2:
                                # 찾았다고 체크 하기
                                sword_check = 1
                                # 검을 가지고 있을 때의 방문체크 배열을 만들기
                                visited2 = [[0] * m for _ in range(n)]
                                q.append((x, y, 2))

    print('Fail')
    return

n, m, t = map(int, input().split())

T = t

arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

visited[0][0] = 1 # 시작위치 방문체크
bfs(0, 0, arr[0][0])





