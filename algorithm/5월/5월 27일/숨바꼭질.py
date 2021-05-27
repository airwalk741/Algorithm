import sys
sys.stdin = open('input (43).txt', 'r')
from collections import deque

def search(subin):

    q = deque()
    q.append(subin)
    cnt = 0
    # 같은 위치인 경우
    if subin == k:
        return cnt

    while q:
        length = len(q)
        cnt += 1
        # 큐 길이만큼 이동
        for _ in range(length):

            num = q.popleft()
            # 최대 거리 안쪽에 있어야 하며 두번 이상 방문하지 않아야한다.
            if 0 <= num - 1 <= 100000 and visited[num-1]:
                if num - 1 == k:
                    return cnt
                visited[num - 1] = 0
                q.append(num-1)

            if 0 <= num + 1 <= 100000 and visited[num+1]:
                if num + 1 == k:
                    return cnt
                visited[num + 1] = 0
                q.append(num+1)

            if 0 <= num * 2 <= 100000 and visited[num * 2]:
                if num * 2 == k:
                    return cnt
                visited[num * 2] = 0
                q.append(num*2)



n, k = map(int, input().split())

visited = [1] * 100001

print(search(n))