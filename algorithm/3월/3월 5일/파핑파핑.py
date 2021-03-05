import sys

sys.stdin = open('input (43).txt', 'r')

# 자기 자신 포함 9 방향
dr = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 0, 1, 1, 1, 0, -1, -1, -1]

# 주위 지뢰가 없는 부분 클릭하면 연쇄작용하는 것으로
# 미로처럼 0을 다 p로 만들어 버린다
def bfs(r,c):

    q = [[r,c]]

    while q:
        num = q.pop(0)

        for k in range(9):
            dx = num[0] + dr[k]
            dy = num[1] + dc[k]
            if 0 <= dx < n and 0 <= dy < n:
                if arr[dx][dy] == 0:
                    arr[dx][dy] = 'p'
                    q.append([dx, dy])


T = int(input())

for tc in range(1, T+1):
    n = int(input())

    arr = [list(input()) for _ in range(n)]

    result = 0

    for i in range(n):
        for j in range(n):
            cnt = 0
            for k in range(9):
                dx = i + dr[k]
                dy = j + dc[k]
                if 0 <= dx < n and 0 <= dy < n:
                    if arr[dx][dy] == '*':
                        cnt += 1
            if arr[i][j] != '*':
                arr[i][j] = cnt


    # 연쇄작용한 클릭 횟수 세는 것
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                bfs(i, j)
                result += 1

    # 연쇄 작용했을 때 주위에 지뢰가 있었으면 0이 아닌 숫자가 나오기때문에
    # 0이 주위에 있었다면 그것의 숫자는 세면 안된다.
    # 0을 bfs에서 p로 바꾸어 줬기 때문에
    # 숫자 주위에 p가 있었다면 연쇄작용했던 숫자였기때문에 클릭횟수를 증가하지 않는다.
    for i in range(n):
        for j in range(n):
            for k in range(9):
                # 지뢰는 클릭하면 안되니까 pass
                if arr[i][j] == '*':
                    break
                dx = i + dr[k]
                dy = j + dc[k]
                if 0 <= dx < n and 0 <= dy < n:
                    if arr[dx][dy] == 'p':
                        break
                        
            # 연쇄 작용이 아닌 숫자였으면 횟수 추가
            else:
                result += 1

    print('#{}'.format(tc), end=' ')
    print(result)










