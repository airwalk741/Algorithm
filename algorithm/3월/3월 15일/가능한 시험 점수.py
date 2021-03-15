import sys

sys.stdin = open('input (43).txt', 'r')

T = int(input())

for tc in range(1, T + 1):

    print('#{}'.format(tc), end=' ')
    n = int(input())

    arr = list(map(int, input().split()))

    result = [0 for _ in range(sum(arr) + 1)]
    result[0] = 1 # 0점 방문 체크
    # 문제 맞춘 점수 방문 체크
    visit = [0]

    for i in arr:
        for j in range(len(visit)):
            if result[i + visit[j]] == 0:
                result[i + visit[j]] = 1
                visit.append(i + visit[j])

    cnt = 0
    for i in result:
        if i != 0:
            cnt += 1

    print(cnt)