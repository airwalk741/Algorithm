import sys
sys.stdin = open('input (43).txt', 'r')
from collections import deque

# 노드 대표 값 찾기
def find_set(x):

    if x == arr[x]:
        return x
    else:
        return find_set(arr[x])

# 대표값 설정
def union(x, y):

    arr[find_set(y)] = find_set(x)


T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    N, E = map(int, input().split())

    arr = [i for i in range(N+1)]
    arrlist = []

    for i in range(E):
        s, e, w = map(int, input().split())

        arrlist.append((s, e, w))

    # 가중치 기준 내림차순 배열
    arrlist.sort(key=lambda x: -x[2])

    result = 0

    for _ in range(E):

        s, e, w = arrlist.pop()

        if find_set(s) != find_set(e):
            union(s, e)
            result += w

    print(arr)
    print(result)
