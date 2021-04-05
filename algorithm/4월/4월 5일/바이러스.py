import sys

sys.stdin = open('input (43).txt', 'r')

def dfs(idx):
    global cnt

    visited[idx] = 1
    s = [idx]

    while len(s):

        num = s.pop()

        for i in range(v+1):
            if computer[num][i] or computer[i][num]:
                if visited[i] == 0:
                    visited[i] = 1
                    s.append(i)
                    cnt += 1

v = int(input())

e = int(input())

arr = [list(map(int, input().split())) for _ in range(e)] # 어떤 것들끼리 공유되어있는지 리스트 받기

computer = [[0] * (v+1) for _ in range(v+1)] # 공유된 컴퓨터

for i in range(len(arr)): # 공유된것 체크
    computer[arr[i][0]][arr[i][1]] = 1



visited = [0] * (v+1) # 방문체크

cnt = 0
dfs(1)
print(cnt)


# 7
# 6
# 1 2
# 2 1
# 1 5
# 5 2
# 5 6
# 4 6