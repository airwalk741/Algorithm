import sys
sys.stdin = open('input (43).txt', 'r')
from collections import deque



## 연산 하기
def operation(idx, screen, clip, cnt):

    if not idx:
        return screen, screen, cnt + 1
    elif idx == 1:
        return screen + clip, clip, cnt + 1
    else:
        return screen - 1, clip, cnt + 1


## 클립 보드랑 스크린이랑 따로이기 때문에 클립 보드 변할 때만 방문체크 -> 구하는게 스크린의 이모티콘 수
## 스크린 변할 때 방문체크를 한다면 연산 1이 q에 들어가지 않는다.
## tc
## 3 1 3
## 3 3 4

def search(screen, clip, cnt):
    global result

    q = deque()
    q.append((screen, clip, cnt))

    while q:

        screen, clip, cnt = q.popleft()

        if screen == S:
            result = cnt
            return

        ## 백트레킹
        if visited[screen] < cnt:
            continue

        for i in range(3):

            x, y, z = operation(i, screen, clip, cnt)

            if x > 0 and x < 1001:
                if not i:
                    if visited[x] >= z:
                        visited[x] = z
                        q.append((x, y, z))
                else:
                    q.append((x, y, z))


S = int(input())

result = 0

visited = [987654321] * 1001

search(1, 0, 0)
print(visited)
print(result)
