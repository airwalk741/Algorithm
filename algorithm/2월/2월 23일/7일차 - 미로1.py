import sys
sys.stdin = open('input (9).txt', 'r')

def dfs(r, c):

    res = 0
    st = []
    st.append((r, c))
    while len(st):
        a, b = st.pop()
        for i in range(4):
            dx = a + dr[i]
            dy = b + dc[i]

            if arr[dx][dy] == 0:
                st.append((dx, dy))
                arr[dx][dy] = 1
            elif arr[dx][dy] == 3:
                res = 1
                break
            print(st)
    return res

for tc in range(1, 11):

    t = int(input())

    arr = [list(map(int, input())) for _ in range(16)]



    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                r = i
                c = j

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]


    print(dfs(r, c))















