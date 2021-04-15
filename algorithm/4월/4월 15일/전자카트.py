import sys
sys.stdin = open('input (43).txt', 'r')

# 행에 따라 열을 한번씩만 택해야한다.
# 맨 마지막은 열의 index가 0이여야한다. (사무실로 돌아오는 것이기 떄문)

def dfs(r, c, num):
    global result
    global visited

    # 방문 길이가 사무실 + 관리구역 - 1 이면 맨 마지막은 사무실로 돌아오는 것이므로
    # 마지막은 arr[r][0]의 값을 더해줘서 최솟값을 찾는다.
    if len(visited) == n-1:
        num += arr[r][0]
        if num < result:
            result = num
        return

    if num > result:
        return

    # 맨 마지막은 사무실 idx = 0 인 곳으로 와야하기때문에 1부터 시작
    for i in range(1, n):
        if arr[r][i] != 0:
            if i not in visited:
                visited.append(i) # 관리구역 방문 체크
                dfs(i, 0, num + arr[r][i])
                visited.remove(i) # 원상 복구

T = int(input())

for tc in range(1, T+1):

    print('#{}'.format(tc), end=' ')
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    result = 987654321

    visited = []

    dfs(0, 0, 0)

    print(result)