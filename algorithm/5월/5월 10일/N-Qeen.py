import sys
sys.stdin = open('input (43).txt', 'r')

def qeen(r, cross, recross, c_visited):
    global cnt

    if r < n+1:

        for c in range(n):
            if r + c not in cross: # 왼쪽 아래에서 오른쪽 위 대각선
                if c - r not in recross: # 왼쪽 위에서 오른쪽 아래 대각선
                    if c not in c_visited: # 열
                        cross.append(r+c)
                        recross.append(c-r)
                        c_visited.append(c)
                        qeen(r+1, cross, recross, c_visited)
                        cross.pop()
                        recross.pop()
                        c_visited.pop()

        # 행이 끝까지 갔으면 N-Qeen 성립
        if r == n:
            cnt += 1


n = int(input())

cnt = 0

for i in range(n):
    qeen(1, [i], [i], [i])

print(cnt)