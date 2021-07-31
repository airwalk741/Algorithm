import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


T = int(input())

for _ in range(T):

    n = int(input())
    # 인덱스 번호 맞춰주기 위해 0을 넣어둔다.
    arr = [0]

    arr += list(map(int, input().split()))

    # 사이클을 형성하고 또 싸이클 안에 있는 숫자 가리키면 굳이 안해도 될 거 하는 거라서 방문체크 해야된다.
    visited = [0] * (n + 1)

    result = 0

    for i in range(1, n + 1):
        # 한번도 체크하지 않은 팀원이라면
        if not visited[i]:
            # 다음을 위해 방문 체크 해두고
            visited[i] = 1
            # 팀으로 들어온 것마다 번호를 1번부터 붙여준다.
            team = {}

            # 팀원들을 모아두는 변수
            s = [i]
            totoal = 1

            while s:

                num = s[-1] # 방금 들어온 팀원이 같이 하고 싶은 팀원 고르는 것 그게 next_num

                next_num = arr[num]

                if next_num == i: # 다음 팀원이 처음 팀원이였다면 사이클 형성
                    break

                if visited[next_num]: # 이미 방문 체크를 해줬다면
                    result += totoal  # team에 있는 팀원들은 낙오나 다름 없음 (사이클이 형성 안되니끼)
                    break

                if next_num in team.keys(): # 다음 팀원이 방문했던 팀원을 가르키면 모든 팀원 사이클 x
                    result += team[next_num] - 1 # 부분 사이클 1 -> 2 -> 3- > 4 -> 5 -> 3
                    break
                else:
                    team[next_num] = totoal + 1

                totoal += 1 # team에 있는 인원 수
                s.append(next_num) # 다음 순번 찾기 위해 넣기

            # team에 있는 팀원들 방문 체크
            for i in s:
                visited[i] = 1


    print(result)