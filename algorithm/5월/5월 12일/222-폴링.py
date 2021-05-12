# import sys
# sys.stdin = open('input (43).txt', 'r')
# import pprint

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

length = n

# 가로 세로 길이가 1이 될때까지 반복
while length != 1:

    result = [] # 2번째로 큰 행렬 모아두는 리스트

    for i in range(0, length, 2):
        col_result = [] # 가로 줄
        for j in range(0, length, 2):
            second = []
            # 2 X 2 행렬
            for x in range(i, i + 2):
                for y in range(j, j + 2):
                    second.append(arr[x][y])

            # 정렬해서 2번째로 큰 값만  col_result에 담기
            second.sort()
            col_result.append(second[2])

        # 가로줄 완성하면 담아두기
        result.append(col_result)

    # 2 x 2 행렬로 해서 찾았으니 가로세로가 2배씩 작아진다.
    length = length // 2

    arr = [] # 다음 행렬 만들기 ( 딥카피? )
    for i in range(length):
        arr.append(list(result[i]))

print(*arr[0])