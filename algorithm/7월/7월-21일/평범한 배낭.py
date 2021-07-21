import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline



def search(idx):


    weigth = dp[idx - 1][0] # 전 단계 최대 무게
    value = dp[idx - 1][1] # 전 단계 최대 가중치

    if weigth + toy[idx][0] <= k: # 더 했는데 k보다 작으면 방문 체크하고 나오기
        visited[idx] = 1
        return (weigth + toy[idx][0], value + toy[idx][1])

    _max = 0
    _value = 0

    for i in range(idx - 1, -1, -1):


        if visited[i]: # 방문했던 것만 빼면서 최댓값 구해보기

            weigth -= toy[i][0]
            value -= toy[i][1]


            if weigth + toy[idx][0] <= k:

                if value + toy[idx][1] >= dp[idx - 1][1]:

                   if _value < value + toy[idx][1]:

                       _max = weigth + toy[idx][0]
                       _value = value + toy[idx][1]

            if value + toy[idx][1] < dp[idx - 1][1]:
                visited[idx] = 1
                return (_max, _value)

    if _max: # 최대가 갱신되었으면 방문체크
        visited[idx] = 1
    return (_max, _value)




n, k = map(int, input().split())

toy = []

remain = 0

for i in range(n):
    w, v = map(int, input().split())
    remain += v
    toy.append((w, v))


visited = [0] * n

toy.sort(key=lambda x: x[0])


dp = [(0, 0)] * n

if toy[0][0] <= k:
    if toy[0][1]:
        dp[0] = (toy[0][0], toy[0][1])
    else:
        dp[0] = (0, 0)
    visited[0] = 1

    for i in range(1, n):

        nw, nv = search(i)

        if dp[i - 1][1] > nv:
            dp[i] = dp[i - 1]
        else:
            dp[i] = (nw, nv)


    print(dp[-1][1])


else:
    print(0)




















