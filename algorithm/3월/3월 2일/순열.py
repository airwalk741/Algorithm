import sys

sys.stdin = open('input (43).txt', 'r')


def dfs(value, _sum):
    global _min
    # value => 행
    # _sum => 구하는 최소값
    # 마지막 열이라면 최솟값을 비교
    if value == n:
        if _sum < _min:
            _min = _sum
        return
    # 백트레킹 ( 굳이 안해도 되는 연산 제거 )
    if _sum >= _min:
        return

    for i in range(n):
        # i번째 열을 쓰지 않았다면
        if visited[i] == 0:
            visited[i] = 1 # 썼다고 하고
            dfs(value + 1, _sum + arr[value][i]) # 다음 행으로 옮기는 재귀함수로
            visited[i] = 0 # 다시 원래대로 
    return _min


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    print('#{}'.format(tc), end=' ')

    arr = [list(map(int, input().split())) for _ in range(n)]

    # 열 방문했는지 안했는지 체크하는 변수
    visited = [0] * n

    _min = 987654321

    print(dfs(0, 0))
