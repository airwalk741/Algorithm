import sys

sys.stdin = open('input (6).txt', 'r')

T = int(input())

for tc in range(1, T+1):

    arr = [list(map(int, input().split())) for _ in range(9)]



    result = 1

    # 행과 열 비교
    for i in range(len(arr)):
        count_r = [1] * 10 # 빈 카운트 배열 (인덱스가 0~9)
        count_c = [1] * 10 # 빈 카운트 배열
        for j in range(len(arr[0])):
            count_r[arr[i][j]] -= 1 # 숫자가 있는 자리의 카운트 -1 해준다
            count_c[arr[j][i]] -= 1
        # 카운트가 0의 자리부터 있어서(인덱스가 0부터) 0은 1이기때문에 1이 아니면 중복이 어떤 수가 중복이 된것이다.
        if count_r.count(1) != 1 or count_c.count(1) != 1:
            result = 0
            break

    # 3 X 3 행렬을 나눈 것
    for x in range(0, 7, 3): # 행 기준 자리 바꾸는 것
        for k in range(0, 7, 3): # 열 기준 자리 바꾸는 것
            count_r = [1] * 10
            for i in range(x, 3+x): # 3 X 3 행
                for j in range(k, 3+k): # 3 X 3 열
                    count_r[arr[i][j]] -= 1

            if count_r.count(1) != 1:
                result = 0
                break
        if result == 0:
            break

    print('#{}'.format(tc), end=' ')
    print(result)















