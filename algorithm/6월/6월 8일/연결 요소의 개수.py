import sys
sys.stdin = open('input (43).txt', 'r')
input = sys.stdin.readline

def dfs(num):

    s = list(nodes[num])
    nodes[num] = 0

    while s:

        next = s.pop()

        if nodes[next]:
            while nodes[next]:
                s.append(nodes[next].pop())


n, m = map(int, input().split())

nodes = [[] for _ in range(1001)]

# 무리 맺은 노드 수 ( 입력에 들어오지 않은 숫자 체크하기 위해 )
cnt = []

for _ in range(m):
    u, v = map(int, input().split())

    if u not in cnt:
        cnt.append(u)
    if v not in cnt:
        cnt.append(v)

    nodes[u].append(v)
    nodes[v].append(u)

result = 0

# 무리의 개수 구하기
for i in range(1, 1001):

    if nodes[i]:
        result += 1
        dfs(i)

# 전체 개수 - 입력한 숫자 수 + 무리의 개수
print(result + n - len(cnt))