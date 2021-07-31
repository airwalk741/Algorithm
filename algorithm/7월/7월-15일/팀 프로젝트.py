import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


T = int(input())

for _ in range(T):

    n = int(input())

    arr = [0]

    arr += list(map(int, input().split()))

    visited = [0] * (n + 1)

    result = 0

    for i in range(1, n + 1):

        if not visited[i]:

            visited[i] = 1

            team = [0] * (n + 1)

            s = [i]
            totoal = 1

            while s:

                num = s[-1]

                next_num = arr[num]

                if next_num == i:
                    break

                if visited[next_num]:
                    result += totoal
                    break

                if team[next_num]:
                    result += team[next_num] - 1
                    break

                team[next_num] = totoal + 1

                totoal += 1
                s.append(next_num)

            for i in s:
                visited[i] = 1


    print(result)