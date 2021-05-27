import sys
sys.stdin = open('input (43).txt', 'r')
input = sys.stdin.readline
from collections import deque

def seach(num):

    q = deque()

    q.append(num)
    cnt = 0
    # 찾는게 나 자신일 수도 있음
    if num == coca:
        return cnt

    # q로 돌면서 cnt 증가
    # q를 현재 길이만큼 돌아야 함
    while q:

        length = len(q)
        cnt += 1
        for _ in range(length):

            me = q.popleft()

            if coca in tree[me]:
                return cnt

            while tree[me]:

                q.append(tree[me].pop())

            for i in range(n):
                if me in tree[i]:
                    if i == coca:
                        return cnt
                    q.append(i)


n = int(input())

pepsi, coca = map(int, input().split())

m = int(input())

tree = [[] for _ in range(n+1)]

# 트리 만들기
for _ in range(m):
    x, y = map(int, input().split())

    tree[x].append(y)

result = seach(pepsi)

# 친척끼리 연결되어 있지 않으면 none값 반환
if result:
    print(result)
else:
    print(-1)






