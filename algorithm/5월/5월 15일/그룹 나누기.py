import sys
sys.stdin = open('input (43).txt', 'r')

def find(x): # 대표 찾기

    if x == replacement[x]:
        return x
    else:
        return find(replacement[x])

def union(x, y): # 대표 입력

    replacement[find(y)] = find(x)


T = int(input())

for tc in range(1, T+1):

    print('#{}'.format(tc), end=' ')

    n, m = map(int, input().split())

    team = [0] * n

    # 조장만 담을 리스트
    replacement = [ i for i in range(n + 1)]

    arr = list(map(int, input().split()))

    # 조장 찾기
    for i in range(0, m*2, 2):

        union(arr[i], arr[i+1])

    # 진짜 조장으로 만들기
    for i in range(n + 1):
        replacement[i] = find(replacement[i])

    # 중복 제거, 0 제거
    print(len(set(replacement)) -1)



















