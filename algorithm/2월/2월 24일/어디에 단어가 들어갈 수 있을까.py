import sys
sys.stdin = open('input (9).txt', 'r')

T = int(input())

for tc in range(1, T+1):

    n, k = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]


    result = 0
    for i in range(n):
        cnt = 0
        result_fake = 0 # 빈 공간이 k보다 많으면 0이 나올때까지 넘긴다.
        for j in range(n):

            if result_fake == 1 and arr[i][j]:
                continue
            else:
                result_fake = 0 # 0이 나왔으므로 다음부터는 1이나오면 cnt 센다

            if arr[i][j] == 1:
                cnt += 1
                if cnt == k:
                    result += 1
                elif cnt > k: # k보다 크면 길이 벗어난거라서 0이 나올때까지 넘김
                    result_fake = 1
                    result -= 1
                    cnt = 0
            else: # 0 이나오면 cnt 다시 센다.
                cnt = 0

    # 행렬 바꿈
    for i in range(n):
        cnt = 0
        result_fake = 0
        for j in range(n):

            if result_fake == 1 and arr[j][i]:
                continue
            else:
                result_fake = 0

            if arr[j][i] == 1:
                cnt += 1
                if cnt == k:
                    result += 1
                elif cnt > k:
                    result_fake = 1
                    result -= 1
                    cnt = 0
            else:
                cnt = 0
    print('#{}'.format(tc), end=' ')
    print(result)











