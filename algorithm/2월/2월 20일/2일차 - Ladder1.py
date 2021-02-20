import sys

sys.stdin = open('input (6).txt', 'r')

for tc in range(1, 11):
    # 사다리게임이기 떄문에 당첨 인것에서 위로 올라가서 선택지를 찾는다
    t = int(input())
    # 인덱스 에러 방지 하기 위해서 왼쪽, 위쪽, 오른쪽에 0을 추가한다.
    puzzle = [[0] * 100]
    puzzle += [[0]+list(map(int, input().split()))+[0] for _ in range(100)]


    for k in range(len(puzzle)):
        j = 100

        # 당첨인 인덱스(열) 찾는 if문
        if puzzle[j][k] == 2:
            i = k

            while j > 1:
                # 왼쪽에 1이 나오면 왼쪽으로 한칸씩 이동한다.
                if puzzle[j][i-1] == 1:
                    i -= 1
                    # 만약 왼쪽으로 한칸 이동했는데 그 위에 1이있으면  while문 나간다.
                    while puzzle[j-1][i] != 1:
                        i -= 1
                # 오른쪽에 1이 나오면 오른쪽으로 한칸씩 이동한다.
                elif puzzle[j][i+1] == 1:
                    i += 1
                    # 만약 위쪽에 1이 있다면 while문을 빠져나간다.
                    while puzzle[j-1][i] != 1:
                        i += 1
                # 오른쪽 혹은 왼쪽으로 이동했을때 다시 돌아가는 것 방지하는 것과
                # 오른쪽 왼쪽이 없다면 위로 올라가게 하기 위해서 -1 해준다.
                j -= 1
            break

    print('#{}'.format(tc), end=' ')
    # 처음에 리스트 만들때 왼쪽에 0 을 추가했으므로 인덱스 하나 빼줘야함
    print(i-1)







