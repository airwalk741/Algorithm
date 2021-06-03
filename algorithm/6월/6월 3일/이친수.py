import sys
sys.stdin = open('input (43).txt', 'r')



n = int(input())

visited = [0] * 91
visited[1] = 1
visited[2] = 1

for i in range(3, 91):
    visited[i] = visited[i-1] + visited[i-2]
    if i > n:
        break

print(visited[n])



