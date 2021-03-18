import sys

sys.stdin = open('input (43).txt', 'r')

# 위로 올리는 것은 배열을 시계 반대 방향으로 90도 돌리고 왼쪽으로 미는 것과 같다.
# 아래로 내리는 것은 배열을 시계 반대 방향으로 90도 돌리고 오른쪽으로 미는 것과 같다.

def game(s):
    global arr

   # 왼쪽으로 미는 것
    if s == 'up' or s == 'left':
        # 0인 것들을 삭제한다
        for i in range(int(n)):
            j = 0
            while j < len(arr[i]):
                if arr[i][j] == 0:
                    arr[i].pop(j)
                else:
                    j += 1

        # 왼쪽 값과 그다음 숫자가 같으면
        # 두개를 더 한값을 앞에 두고 두번째 값은 지운다
        # while문 나가면 같은 같들 다 찾은거니까 나머지는 0으로 채운다.
        for i in range(int(n)):
            j = 0
            while j < len(arr[i])-1:
                if arr[i][j] == arr[i][j + 1]:
                    arr[i][j] += arr[i][j]
                    arr[i].pop(j + 1)


                j += 1
            # 나머지 0으로 채우는 것
            arr[i] = arr[i] + [0] * (int(n) - len(arr[i]))



    # 오른쪽으로 미는 것!
    elif s == 'down' or s == 'right':

        # 0인 것들을 삭제한다
        for i in range(int(n)):
            for j in range(int(n) - 1, -1, -1):
                if arr[i][j] == 0:
                    arr[i].pop(j)

        # 제일 오른쪽과 그 전 오른쪽이 같다면
        # 제일 오른쪽을 2배 해주고
        # 그 전 오른쪽은 삭제해준다
        for i in range(len(arr)):
            j = len(arr[i]) - 1
            while j > 0:
                if arr[i][j] == arr[i][j-1]:
                    arr[i][j] *= 2
                    arr[i].pop(j-1)
                    j -= 1

                j -= 1

            # 다 오른쪽으로 밀었을때 빈곳은 0으로 채워줘야한다
            arr[i] = [0] * (int(n) - len(arr[i])) + arr[i]

    # 시계반대방향으로 돌려줬던 것을 원래대로 돌려준다
    arr2 = []
    if s == 'up' or s == 'down':

        for i in range(int(n)):
            arr3 = []
            for j in range(int(n) - 1, -1, -1):
                arr3.append(arr[j][i])
            arr2.append(arr3)

        arr = arr2

T = int(input())

for tc in range(1, 1 + T):

    n, s = input().split()

    arr = [list(map(int, input().split())) for _ in range(int(n))]

    # 위로 올리는 것은 배열을 시계 반대 방향으로 90도 돌리고 왼쪽으로 미는 것과 같다.
    # 아래로 내리는 것은 배열을 시계 반대 방향으로 90도 돌리고 오른쪽으로 미는 것과 같다.

    arr2 = []
    if s == 'up' or s == 'down':
        for i in range(int(n) - 1, -1, -1):
            arr3 = []
            for j in range(int(n)):
                arr3.append(arr[j][i])
            arr2.append(arr3)

        arr = arr2

    game(s)

    print('#{}'.format(tc))

    for i in range(int(n)):
        print(*arr[i])



