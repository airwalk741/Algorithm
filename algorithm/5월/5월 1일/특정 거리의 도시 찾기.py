import sys
# sys.stdin = open('input (43).txt', 'r')
from collections import deque
input = sys.stdin.readline

# 다익스트라
def bfs(idx):
    q = deque()

    q.append(idx)

    while q:
        num = q.popleft() # 딕셔너리 key는 str
        start = int(num) # 리스트 인덱스는 int

        # 시작 -> 끝 이렇게 찾으면 다음 갈 경로는
        # 끝이 시작으로 된다
        # 1 -> 2 라면  다음 q는
        # 2 -> 어떠한 노드  그 다음 q는
        # 어떠한 노드 -> 다른 어떠한 노드
        if num in arr.keys():
            cycle = arr[num]
        else: # 끝 노드가 시작이 되야하는데 시작이 되야하는 노드(키)가 없으면 continue
            continue

        # cycle은 시작(키)의 value => 도착 노드들
        for e in cycle:
            end = int(e)
            # 다익스트라
            if visited[end] > visited[start] + 1:
                visited[end] = visited[start] + 1
                if visited[end] <= k:
                    q.append(e)


n, m, k, x = map(int, input().split())

# key : 시작 노드
# value : 도착 노드
arr = {}

for _ in range(m):
    s, e = input().split()
    # 시작노드가 없었으면 만들어서 끝노드 list에 담아서 dic 완성
    if s in arr.keys():
        arr[s] += [e]
    else:
        arr[s] = [e]

# print(arr)

# 다익스트라 방문 체크
visited = [987654321] * (n + 1)
visited[x] = 0

bfs(str(x))
# k와 같은게 있는지 없는지 체크하기 위해 res 변수 생성
res = 1


while True:

    # index 함수 이용하는데 k 값이 없으면 while 나가기
    try:
        number = visited.index(k)
        res = 0 # k가 있었으므로 체크하기
    except:
        break

    print(number)
    # index 함수는 앞에서부터 한개 찾는거여서 찾았으면 바꿔주기
    visited[number] = 987654321

# k 값 없었으면 -1 출력
if res:
    print(-1)



